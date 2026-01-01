#!/usr/bin/env python3
"""
mcp_server.py — Auto-register every demo script in ./tools as its own MCP tool.

Each tool runs exactly one script:
  - Tool name: sm0l_<filename_stem>
  - Tool description: derived from the script's module docstring or first comment line
  - Tool inputs: args(list[str]), timeout_s(int), workdir(str|None), env(dict[str,str]|None)
  - Tool output: dict(exit_code, stdout, stderr, duration_ms, script)

This is intentionally "script runner" style because the demo scripts are heterogeneous:
some are CLIs, some open windows, some require optional deps, some just print.

Transport: stdio (perfect for local testing / MCP clients).
"""

from __future__ import annotations

import os
import re
import sys
import time
import json
import types
import pathlib
import subprocess
from typing import Any, Dict, List, Optional

from fastmcp import FastMCP


TOOLS_DIR = pathlib.Path(__file__).resolve().parent / "tools"


# minimal module->package mapping (extend as needed)
MOD_TO_PKG = {
    "bs4": "beautifulsoup4",
    "sklearn": "scikit-learn",
    "yaml": "PyYAML",
    "PIL": "Pillow",
    "fitz": "PyMuPDF",
    "sentence_transformers": "sentence-transformers",
    "plotly_resampler": "plotly-resampler",
    "youtubesearchpython": "youtube-search-python",
}

# extras->packages mapping (load from pyproject OR bake it)
EXTRAS_TO_PKGS = {
    "web": {"requests","httpx","urllib3","beautifulsoup4","fastapi","Flask"},
    "browser": {"playwright","selenium","pyppeteer"},
    "viz": {"matplotlib","plotly","seaborn","mplcursors","pydeck","pyecharts","plotext"},
    "bigviz": {"datashader","holoviews"},
    "nlp": {"textblob"},
    "spacy": {"spacy"},
    "embeddings": {"sentence-transformers"},
    "torch": {"torch"},
    "doc": {"PyPDF2","PyMuPDF","pdfplumber","openpyxl","fpdf2"},
    "ocr": {"pytesseract"},
    "audio": {"pydub"},
    "auto": {"APScheduler","schedule"},
    "workflows": {"prefect","dagster"},
    "sys": {"psutil","watchdog"},
}

def _missing_module_from_stderr(stderr: str) -> Optional[str]:
    # Matches: ModuleNotFoundError: No module named 'xyz'
    m = re.search(r"No module named ['\"]([A-Za-z0-9_\.]+)['\"]", stderr)
    if not m:
        return None
    return m.group(1).split(".")[0]

def _install_hints_for_module(mod: str) -> Dict:
    pkg = MOD_TO_PKG.get(mod, mod)  # fallback guess: package == module
    extras = sorted([e for e, pkgs in EXTRAS_TO_PKGS.items() if pkg in pkgs])
    hints = {
        "missing_module": mod,
        "suggested_pypi": pkg,
        "suggested_extras": extras,
        "pip_commands": [],
        "notes": [],
    }

    # Prefer extras in your repo context:
    if extras:
        hints["pip_commands"].append(f"pip install -e .[{','.join(extras)}]")
        hints["notes"].append("Preferred: install via extras for reproducible capability bundles.")
    else:
        hints["pip_commands"].append(f"pip install {pkg}")
        hints["notes"].append("Fallback: install the missing package directly.")

    # system-deps reminders
    if pkg == "pytesseract":
        hints["notes"].append("OCR also needs the system 'tesseract' binary installed and on PATH.")
    if pkg == "pydub":
        hints["notes"].append("Audio often needs ffmpeg installed and on PATH.")
    if pkg == "playwright":
        hints["pip_commands"].append("playwright install")
        hints["notes"].append("Playwright needs browser binaries installed via 'playwright install'.")

    return hints


def _read_tool_description(py_path: pathlib.Path) -> str:
    """
    Best-effort description:
      1) module docstring (triple-quoted at top)
      2) first non-empty comment line
      3) fallback: "Run <filename>"
    """
    try:
        text = py_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return f"Run {py_path.name}"

    # module docstring at top
    m = re.match(r'^\s*(?P<q>["\']{3})(?P<body>.*?)(?P=q)', text, flags=re.DOTALL)
    if m:
        body = m.group("body").strip()
        if body:
            # keep it short for LLM tool lists
            body = re.sub(r"\s+", " ", body)
            return body[:240]

    # first non-empty comment
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            s = s.lstrip("#").strip()
            if s:
                return s[:240]
        break

    return f"Run {py_path.name}"


def _safe_tool_name(stem: str) -> str:
    # MCP tool names should be simple and stable: letters, digits, underscores.
    s = stem.lower()
    s = re.sub(r"[^a-z0-9_]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    if not s:
        s = "tool"
    return f"sm0l_{s}"


def _merge_env(extra: Optional[Dict[str, str]]) -> Dict[str, str]:
    env = dict(os.environ)
    if extra:
        for k, v in extra.items():
            if not isinstance(k, str) or not isinstance(v, str):
                raise ValueError("env must be a dict[str,str]")
            env[k] = v
    return env


def _run_script(
    script_path: pathlib.Path,
    args: List[str],
    timeout_s: int,
    workdir: Optional[str],
    env: Optional[Dict[str, str]],
) -> Dict[str, Any]:
    if timeout_s <= 0:
        raise ValueError("timeout_s must be > 0")

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    # Use the current interpreter to avoid mismatch with venvs.
    cmd = [sys.executable, str(script_path), *args]

    t0 = time.perf_counter()
    try:
        p = subprocess.run(
            cmd,
            cwd=workdir or None,
            env=_merge_env(env),
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
        dt_ms = int((time.perf_counter() - t0) * 1000)
        return {
            "script": script_path.name,
            "exit_code": int(p.returncode),
            "stdout": p.stdout,
            "stderr": p.stderr,
            "duration_ms": dt_ms,
            "cmd": cmd,
            "workdir": workdir,
        }
    except subprocess.TimeoutExpired as e:
        dt_ms = int((time.perf_counter() - t0) * 1000)
        return {
            "script": script_path.name,
            "exit_code": -1,
            "stdout": (e.stdout or ""),
            "stderr": (e.stderr or "") + f"\nTIMEOUT after {timeout_s}s",
            "duration_ms": dt_ms,
            "cmd": cmd,
            "workdir": workdir,
        }


def build_server() -> FastMCP:
    mcp = FastMCP("sm0l-tools-bulk-server")

    @mcp.tool
    def list_sm0l_tools() -> Dict[str, Any]:
        """List all discovered sm0l demo scripts and their mapped MCP tool names."""
        scripts = []
        for py in sorted(TOOLS_DIR.glob("*.py")):
            scripts.append(
                {
                    "script": py.name,
                    "tool": _safe_tool_name(py.stem),
                    "description": _read_tool_description(py),
                }
            )
        return {"count": len(scripts), "tools": scripts}

        result = {
            "script": script_path.name,
            "exit_code": int(p.returncode),
            "stdout": p.stdout,
            "stderr": p.stderr,
            "duration_ms": dt_ms,
            "cmd": cmd,
            "workdir": workdir,
        }

# If it looks like a missing dependency, add install hints:
missing = _missing_module_from_stderr(result["stderr"])
if missing:
    result["install_hints"] = _install_hints_for_module(missing)

return result



    # Register one tool per script
    for script_path in sorted(TOOLS_DIR.glob("*.py")):
        tool_name = _safe_tool_name(script_path.stem)
        desc = _read_tool_description(script_path)

        # Build a distinct function object so FastMCP sees unique names/docstrings.
        def _make_tool(sp: pathlib.Path, description: str):
            def _tool(
                args: List[str] = [],
                timeout_s: int = 60,
                workdir: Optional[str] = None,
                env: Optional[Dict[str, str]] = None,
            ) -> Dict[str, Any]:
                """
                Auto-generated tool wrapper.
                """
                # Validate args are strings (MCP clients sometimes send weird JSON)
                if not isinstance(args, list) or any(not isinstance(x, str) for x in args):
                    raise ValueError("args must be a list of strings")
                return _run_script(sp, args=args, timeout_s=timeout_s, workdir=workdir, env=env)

            _tool.__name__ = tool_name  # unique per script
            _tool.__doc__ = f"{description}\n\nRuns: {sp.name}"
            return _tool

        tool_fn = _make_tool(script_path, desc)

        # FastMCP's decorator is callable, so we can register dynamically.
        # Equivalent to: @mcp.tool
        mcp.tool(tool_fn)

    return mcp


def main() -> None:
    if not TOOLS_DIR.exists():
        raise SystemExit(f"Missing tools directory: {TOOLS_DIR}\nExpected ./tools next to mcp_server.py")

    mcp = build_server()
    # Local-friendly transport (as shown in the tutorial PDF)
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
