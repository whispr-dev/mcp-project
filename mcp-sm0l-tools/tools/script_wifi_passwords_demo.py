"""Wi-Fi password recovery demo (Windows-only).

Uses `netsh` to list profiles and show keys.
"""

import platform, subprocess, re

def main():
    if platform.system() != "Windows":
        print("This demo targets Windows netsh.")
        return

    out = subprocess.check_output(["netsh", "wlan", "show", "profiles"], text=True, errors="ignore")
    profiles = re.findall(r"All User Profile\s*:\s*(.+)", out)

    for name in map(str.strip, profiles):
        info = subprocess.check_output(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                       text=True, errors="ignore")
        key = re.search(r"Key Content\s*:\s*(.+)", info)
        print(name, "=>", key.group(1).strip() if key else "(no key)")

if __name__ == "__main__":
    main()
