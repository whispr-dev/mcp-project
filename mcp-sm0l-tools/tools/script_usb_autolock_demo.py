"""Auto-lock workstation on USB removal (platform-aware skeleton).

This demo only shows lock logic.
Wire it to your preferred device watcher.

Windows lock:
  rundll32.exe user32.dll,LockWorkStation
"""

import platform, subprocess

def lock():
    if platform.system() == "Windows":
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])
    else:
        print("Lock not implemented for", platform.system())

def main():
    print("Call lock() when your USB-removal event fires.")
    lock()

if __name__ == "__main__":
    main()
