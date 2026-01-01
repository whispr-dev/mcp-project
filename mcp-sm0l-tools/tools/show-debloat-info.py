import subprocess
import sys
import os

def _get_powershell_data(command):
    """Helper to run a small PowerShell command and return its output."""
    try:
        # Execute PowerShell command and capture stdout
        result = subprocess.run(
            ["powershell", "-Command", command],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "N/A"
    except FileNotFoundError:
        print("❌ Error: PowerShell not found. Cannot collect data.", file=sys.stderr)
        sys.exit(1)

def show_debloat_info():
    """Gathers and displays system statistics relevant to debloating/performance."""

    # --- Data Collection (Approximated using available tools) ---
    
    # Get RAM Data (Requires PowerShell for easy access)
    total_ram_gb = _get_powershell_data("((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB)")
    ram_used_gb = _get_powershell_data("(((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory - (Get-CimInstance Win32_ComputerSystem).FreePhysicalMemory) / 1GB)")
    
    # Get Process Count
    num_processes = _get_powershell_data("(Get-Process).Count")
    
    # Get Storage Data for SystemDrive (C:)
    try:
        system_drive = os.environ.get('SystemDrive', 'C:')
        # Use simple wmic for storage info
        wmic_output = subprocess.run(
            ["wmic", "logicaldisk", "where", f"DeviceID='{system_drive}:'", "get", "FreeSpace,Size", "/value"], 
            capture_output=True, text=True, check=True
        ).stdout
        
        data = dict(line.split('=', 1) for line in wmic_output.strip().split('\n') if '=' in line)
        total_storage_gb = float(data.get('Size', 0)) / (1024**3)
        free_storage_gb = float(data.get('FreeSpace', 0)) / (1024**3)
        used_storage_gb = total_storage_gb - free_storage_gb
    except Exception:
        total_storage_gb, used_storage_gb = 0, 0

    # Get Services Data (Simplified via PowerShell)
    total_services = _get_powershell_data("(Get-Service).Count")
    disabled_services = _get_powershell_data("(Get-Service | Where-Object StartType -Like \"Disabled\").Count")

    # --- Display ---
    print("\n------------------ System Debloat Summary ------------------")
    print(f"Total Services: {total_services}")
    print(f"Disabled Services: {disabled_services}")
    print("----------------------------------------------------------")
    print(f"Number of Processes: {num_processes}")
    
    try:
        total_ram = float(total_ram_gb)
        used_ram = float(ram_used_gb)
        ram_percent = (used_ram / total_ram) * 100
        print(f"RAM Used: {used_ram:.1f}/{total_ram:.1f} GB ({ram_percent:.1f}%)")
    except ValueError:
        print(f"RAM Used: {ram_used_gb}/{total_ram_gb} GB")

    if total_storage_gb > 0:
        storage_percent = (used_storage_gb / total_storage_gb) * 100
        print(f"Storage Used ({system_drive}): {used_storage_gb:.1f}/{total_storage_gb:.1f} GB ({storage_percent:.1f}%)")
    else:
        print("Storage Used: N/A")
    print("----------------------------------------------------------\n")

if __name__ == "__main__":
    # Note: Full data collection (UWP apps, Win features) requires complex COM/WinRT access 
    # not available via simple Python standard library tools, thus using subprocess/WMIC/PS.
    show_debloat_info()