"""ruff CLI demo on a tiny temp file."""

import subprocess, tempfile, pathlib, textwrap

def main():
    code = "import os\n\nprint(  1+1 )\n"
    p = pathlib.Path(tempfile.mkdtemp())/"bad.py"
    p.write_text(code, encoding="utf-8")
    try:
        r = subprocess.run(["ruff", "check", str(p)], capture_output=True, text=True)
    except FileNotFoundError:
        print("ruff not found. Install ruff and ensure it's on PATH.")
        return
    print((r.stdout or r.stderr).strip() or "ok")

if __name__ == "__main__":
    main()
