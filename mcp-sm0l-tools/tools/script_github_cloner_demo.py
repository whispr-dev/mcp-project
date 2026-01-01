"""GitHub repo cloner skeleton (safe).

Set:
  GITHUB_CLONE_LIST  (comma-separated git URLs)
  GITHUB_CLONE_DIR   (target folder)

This demo will clone missing repos and skip existing ones.
"""

import os, subprocess, pathlib

def main():
    urls = [u.strip() for u in os.getenv("GITHUB_CLONE_LIST", "").split(",") if u.strip()]
    base = pathlib.Path(os.getenv("GITHUB_CLONE_DIR", ""))
    if not urls or not str(base):
        print("Set GITHUB_CLONE_LIST and GITHUB_CLONE_DIR.")
        return

    base.mkdir(parents=True, exist_ok=True)

    def name_of(url):
        s = url.rstrip("/").split("/")[-1]
        return s[:-4] if s.endswith(".git") else s

    for url in urls:
        dest = base / name_of(url)
        if dest.exists():
            print(dest.name, "exists")
            continue
        p = subprocess.run(["git", "clone", "--depth", "1", url, str(dest)],
                           capture_output=True, text=True)
        print(dest.name, "ok" if p.returncode == 0 else "fail")

if __name__ == "__main__":
    main()
