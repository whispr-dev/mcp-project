import subprocess
import sys

def restart_advanced_mode():
    """
    Executes the Windows shutdown command to immediately restart the 
    computer into the Advanced Startup Options menu (WinRE).
    
    Equivalent to: shutdown -o -r -f -t 0
    """
    print("🚀 Preparing to restart into Advanced Startup Mode...")

    # Arguments for the shutdown command:
    # -o: Go to the advanced boot options menu.
    # -r: Restart the computer.
    # -f: Force running applications to close without warning.
    # -t 0: Set the time-out period to 0 seconds (immediate execution).
    command = ["shutdown", "-o", "-r", "-f", "-t", "0"]
    
    try:
        # Execute the command. check=True will raise an error for non-zero exit code.
        subprocess.run(command, check=True, text=True)
        print("\n✅ Command sent successfully. The computer will now restart...")
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ FAILED to execute command.", file=sys.stderr)
        print(f"   Error: {e}. Check if you have the necessary privileges.", file=sys.stderr)
    except FileNotFoundError:
        print("\n❌ Error: The 'shutdown' command was not found. This script is for Windows OS.", file=sys.stderr)

if __name__ == "__main__":
    restart_advanced_mode()