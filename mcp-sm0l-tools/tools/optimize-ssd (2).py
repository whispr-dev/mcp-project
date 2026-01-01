import subprocess
import sys

def optimize_ssd():
    """
    Optimizes SSD life on Windows by disabling unnecessary write operations.
    
    NOTE: This script must be run with Administrator privileges for the 
    'fsutil' commands to succeed.
    """
    print("🚀 Starting SSD Optimization...")

    # fsutil behavior set DisableLastAccess 1
    # Action: Disables Last Access Time stamping to reduce disk I/O, 
    # which is a common SSD life improvement tweak.
    cmd_disable_last_access = ["fsutil", "behavior", "set", "DisableLastAccess", "1"]
    _execute_command(cmd_disable_last_access, "Disable Last Access Time")

    # fsutil behavior set EncryptPagingFile 0
    # Action: Disables Paging File Encryption to reduce CPU overhead and write 
    # amplification.
    cmd_disable_encrypt_paging = ["fsutil", "behavior", "set", "EncryptPagingFile", "0"]
    _execute_command(cmd_disable_encrypt_paging, "Disable Paging File Encryption")

    print("\n✅ SSD Optimization Script finished.")


def _execute_command(cmd, task_name):
    """Executes a command and handles success/error reporting."""
    cmd_str = ' '.join(cmd)
    print(f"\n-> Executing: {task_name}...")
    try:
        # We use 'shell=True' for simplicity in executing native Windows commands,
        # but capture_output=True and check=True to handle errors gracefully.
        result = subprocess.run(cmd, check=True, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print(f"   Success: {task_name} applied.")
        else:
             # Should be caught by check=True, but included for completeness
            print(f"   ⚠️ Warning executing {task_name}: {result.stderr.strip()}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"   ❌ FAILED to execute {task_name}.", file=sys.stderr)
        print("      * Error details: Command failed. You must run this script as **Administrator**.", file=sys.stderr)
    except FileNotFoundError:
        print(f"   ❌ Error: Command '{cmd[0]}' not found. This script is for Windows.", file=sys.stderr)


if __name__ == "__main__":
    optimize_ssd()