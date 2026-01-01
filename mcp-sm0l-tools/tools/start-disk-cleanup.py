import subprocess
import sys
import os
import winreg as reg
from pathlib import Path

def start_disk_cleanup(silent=False):
    """
    Cleans up the WinSxS folder and optionally runs Disk Cleanup (cleanmgr).
    Requires Administrator privileges.
    """
    # 1. Clean the WinSxS folder using DISM
    print("Cleaning the WinSxS folder (This may take a while)...")
    try:
        # DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase
        subprocess.run(
            ["dism", "/Online", "/Cleanup-Image", "/StartComponentCleanup", "/ResetBase"], 
            check=True, 
            capture_output=True, 
            text=True
        )
        print("✅ WinSxS folder cleanup completed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during DISM cleanup (Requires Admin): {e.stderr}", file=sys.stderr)
        return

    # 2. Run cleanmgr.exe
    if not silent:
        print("Starting Disk Cleanup GUI (cleanmgr.exe)...")
        try:
            # Start cleanmgr.exe with arguments to run on the system drive
            subprocess.run(["cleanmgr.exe", f"/d {os.environ.get('SystemDrive', 'C:')}"], shell=True)
            print("Disk Cleanup GUI initiated.")
        except FileNotFoundError:
            print("❌ Error: 'cleanmgr.exe' not found.", file=sys.stderr)
    else:
        # --- Silent Cleanup via Registry Manipulation ---
        print("Starting Disk Cleanup in SILENT mode via Registry...")
        clean_options = [
            "Active Setup Temp Folders", "D3D Shader Cache", "Delivery Optimization Files",
            "Downloaded Program Files", "Internet Cache Files", "Recycle Bin",
            "Temporary Files", "Temporary Setup Files", "Thumbnail Cache", "Update Cleanup"
        ]
        
        reg_path_base = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches"
        
        try:
            # Set StateFlags0777 to 2 for all desired clean options
            for key in clean_options:
                full_path = Path(reg_path_base) / key
                with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, str(full_path)) as hkey:
                    # Value '2' means selected for silent cleanup
                    reg.SetValueEx(hkey, "StateFlags0777", 0, reg.REG_DWORD, 2)
            
            # Start cleanmgr.exe with the /sageset (2) and /sagerun (2) flags
            subprocess.run(["cleanmgr.exe", "/sagerun:2"], check=True, shell=True)
            print("✅ Silent Disk Cleanup completed.")

        except PermissionError:
            print("❌ Error: Registry modification requires Administrator privileges.", file=sys.stderr)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running cleanmgr.exe: {e}", file=sys.stderr)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Windows Disk Cleanup Script.")
    parser.add_argument("--silent", action="store_true", help="Run cleanmgr in silent mode.")
    args = parser.parse_args()
    start_disk_cleanup(args.silent)