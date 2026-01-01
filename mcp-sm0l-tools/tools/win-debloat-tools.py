import subprocess
import sys
import os
import winreg as reg
import ctypes
from enum import Enum

# --- Windows API / Admin Check ---
def check_admin():
    """Checks if the script is running with Administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def request_admin_privilege():
    """Reruns the script as Administrator if not already running as one."""
    if check_admin():
        return True
    
    print("Requesting Administrator privileges...")
    try:
        # Re-launch script with elevated privileges
        params = f'"{sys.executable}" {" ".join(sys.argv)}'
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        sys.exit(0)
    except Exception as e:
        print(f"❌ Failed to request admin rights: {e}", file=sys.stderr)
        return False

# --- Core Tweak Functions (Simplified) ---

def enable_dark_mode():
    """Sets Windows to use Dark Mode via Registry."""
    print("Setting Dark Mode...")
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
        
        # App theme (0=Light, 1=Dark)
        with reg.CreateKey(reg.HKEY_CURRENT_USER, key_path) as key:
            reg.SetValueEx(key, "AppsUseLightTheme", 0, reg.REG_DWORD, 0)
        
        # System theme (0=Light, 1=Dark)
        with reg.CreateKey(reg.HKEY_CURRENT_USER, key_path) as key:
            reg.SetValueEx(key, "SystemUsesLightTheme", 0, reg.REG_DWORD, 0)
        
        print("✅ Dark Mode enabled (may require restart or re-login).")
    except Exception as e:
        print(f"❌ Error setting Dark Mode: {e}", file=sys.stderr)

def disable_cortana():
    """Disables Cortana via Registry."""
    print("Disabling Cortana...")
    try:
        key_path = r"SOFTWARE\Policies\Microsoft\Windows\Windows Search"
        with reg.CreateKey(reg.HKEY_LOCAL_MACHINE, key_path) as key:
            reg.SetValueEx(key, "AllowCortana", 0, reg.REG_DWORD, 0)
        print("✅ Cortana disabled.")
    except Exception as e:
        print(f"❌ Error disabling Cortana (Requires Admin): {e}", file=sys.stderr)

def remove_uwp_apps():
    """Removes select UWP provisioned packages using PowerShell subprocess."""
    # List of apps to remove (example subset)
    apps_to_remove = ["Microsoft.ZuneVideo", "Microsoft.BingNews", "Microsoft.WindowsAlarms"]
    
    print("Removing UWP Apps...")
    try:
        # Command to get package, remove it, and remove provisioned package
        powershell_command = (
            "$apps = @('{apps}'); "
            "foreach ($app in $apps) {{ "
                "Get-AppxPackage -Name $app | Remove-AppxPackage -ErrorAction SilentlyContinue; "
                "Get-AppxProvisionedPackage -Online | Where-Object {{ $_.DisplayName -like \"*$app*\" }} | Remove-AppxProvisionedPackage -Online -ErrorAction SilentlyContinue "
            "}}"
        ).format(apps="', '".join(apps_to_remove))

        subprocess.run(["powershell", "-Command", powershell_command], check=True, shell=True)
        print(f"✅ Removed: {', '.join(apps_to_remove)}.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error removing UWP apps (Requires Admin): {e}", file=sys.stderr)


# --- Main CLI Menu ---

class MenuOption(Enum):
    THEME = 1
    CORTANA = 2
    UWP = 3
    EXIT = 4

def main_menu():
    print("\n--- 🚀 Win Debloat Tools (CLI) ---")
    if not check_admin():
        print("⚠️ Warning: Not running as Administrator. Some options will fail.")
        
    while True:
        print("\nSelect an action:")
        print(f"  {MenuOption.THEME.value}. Enable Dark Mode")
        print(f"  {MenuOption.CORTANA.value}. Disable Cortana")
        print(f"  {MenuOption.UWP.value}. Remove Basic UWP Apps (Requires Admin)")
        print(f"  {MenuOption.EXIT.value}. Exit")
        
        try:
            choice = int(input("Enter number: "))
            
            if choice == MenuOption.THEME.value:
                enable_dark_mode()
            elif choice == MenuOption.CORTANA.value:
                disable_cortana()
            elif choice == MenuOption.UWP.value:
                remove_uwp_apps()
            elif choice == MenuOption.EXIT.value:
                print("Exiting.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Enter a number.")

if __name__ == "__main__":
    if not check_admin():
        # Optional: prompt to re-launch as admin
        print("This tool works best with Administrator privileges.")
    
    main_menu()