import subprocess
import sys

def restart_advanced_mode():
    """
    Restarts the computer immediately into the Advanced Startup options menu.
    Requires Administrator privileges.
    """
    try:
        # shutdown -o: Reboot into Advanced options. 
        # -r: Restart. -f: Force apps to close. -t 0: Immediate.
        subprocess.run(["shutdown", "-o", "-r", "-f", "-t", "0"], check=True, shell=True)
        print("Initiating restart to Advanced Mode...")
    except subprocess.CalledProcessError as e:
        # This often fails if the user is not an administrator
        print(f"❌ Error initiating shutdown (Requires Admin): {e}", file=sys.stderr)
    except FileNotFoundError:
        print("❌ Error: 'shutdown' command not found. This is highly unusual.", file=sys.stderr)

if __name__ == "__main__":
    restart_advanced_mode()