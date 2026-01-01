from __future__ import annotations
import subprocess, tempfile, pathlib, textwrap, shutil

if __name__ == "__main__":
    if not shutil.which("ruff"):
        print("Ruff not found. Install with: pip install ruff")
        raise SystemExit(0)
    code = "import os\n\nprint(  1+1)\n"
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "bad.py"
        p.write_text(code)
        r = subprocess.run(["ruff", "check", str(p)], capture_output=True, text=True)
        print(r.stdout.strip() or "No issues?")
