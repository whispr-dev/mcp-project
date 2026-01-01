"""scdl safe demo: print CLI help.

This does not download anything.
"""

import subprocess, sys

def main():
    try:
        p = subprocess.run(["scdl", "--help"], capture_output=True, text=True)
    except FileNotFoundError:
        print("scdl CLI not found. Install scdl and ensure it's on PATH.")
        return
    print((p.stdout or p.stderr).splitlines()[0] if (p.stdout or p.stderr) else "ok")

if __name__ == "__main__":
    main()
