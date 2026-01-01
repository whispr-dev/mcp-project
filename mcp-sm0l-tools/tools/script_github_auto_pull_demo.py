"""GitHub repo auto-pull demo (safe).

Set:
  GITHUB_REPOS_DIR  (folder containing git repos)
"""

import os, subprocess, pathlib

def main():
    base = pathlib.Path(os.getenv("GITHUB_REPOS_DIR", ""))
    if not base.is_dir():
        print("Set GITHUB_REPOS_DIR to a folder of git repos.")
        return

    def is_repo(p): return (p / ".git").exists()

    repos = [p for p in base.iterdir() if p.is_dir() and is_repo(p)]
    if not repos:
        print("no repos found")
        return

    for r in repos:
        p = subprocess.run(["git", "-C", str(r), "pull", "--ff-only"],
                           capture_output=True, text=True)
        print(r.name, "ok" if p.returncode == 0 else "fail")

if __name__ == "__main__":
    main()
