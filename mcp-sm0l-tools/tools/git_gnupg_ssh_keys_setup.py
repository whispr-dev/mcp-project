import subprocess
import sys
import os
import shutil
from pathlib import Path

# Define necessary paths
GIT_BIN = shutil.which("git")
GPG_BIN = shutil.which("gpg")
SSH_FOLDER = Path.home() / ".ssh"
GPG_FOLDER = Path.home() / ".gnupg"

def check_admin():
    """Returns True if the script is running with Administrator privileges."""
    try:
        # Check if the user has been granted SE_DEBUG_PRIVILEGE, common proxy for admin check
        return os.getuid() == 0 
    except AttributeError:
        # Windows-specific check using ctypes
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()

def _run_git_config(prop_name, prop_value=None):
    """Helper to run git config commands."""
    cmd = [GIT_BIN, "config", "--global", prop_name]
    if prop_value:
        cmd.append(prop_value)
    
    print(f"Executing: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True, shell=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error setting git config {prop_name}: {e}", file=sys.stderr)
        return False

def initialize_git_user():
    """Prompts for and sets global Git user name and email."""
    print("--- Git User Setup ---")
    
    # Set User Name
    name = input("Enter your full Git user name (e.g., Jane Doe): ").strip()
    if name:
        _run_git_config("user.name", name)
        
    # Set User Email
    email = input("Enter your Git email address: ").strip()
    if email:
        _run_git_config("user.email", email)

def enable_ssh_and_gpg_agent():
    """Sets up the GPG agent to handle keys."""
    if not GPG_BIN:
        print("❌ GPG not found. Cannot configure agent.", file=sys.stderr)
        return
        
    print("\nEnabling GPG/SSH Agent...")
    try:
        # Start gpg-agent and set it for Git (or similar steps in Python)
        # The PowerShell script relies on tools installed by the manager.
        # Minimal Python equivalent: Ensure gpg.program is set for Windows Git to find gpg
        _run_git_config("gpg.program", "C:/Program Files/Git/usr/bin/gpg.exe") # Common Git path
        print("✅ GPG program set for Git.")
    except Exception as e:
        print(f"❌ Error configuring GPG Agent: {e}", file=sys.stderr)

def set_ssh_key():
    """Creates a new SSH key pair."""
    print("\n--- SSH Key Creation ---")
    
    # Use ssh-keygen command
    ssh_keygen_cmd = [shutil.which("ssh-keygen"), "-t", "ed25519", "-C", input("Enter comment for new key (usually your email): ")]
    print(f"Executing: {' '.join(ssh_keygen_cmd)}")
    try:
        # This will be interactive, user must input path and passphrase
        subprocess.run(ssh_keygen_cmd, check=False)
        print("✅ SSH key creation sequence completed.")
    except Exception as e:
        print(f"❌ Error running ssh-keygen: {e}", file=sys.stderr)

def set_gpg_key():
    """Creates a new GPG key pair."""
    if not GPG_BIN:
        print("❌ GPG not found. Cannot create key.", file=sys.stderr)
        return
        
    print("\n--- GPG Key Creation ---")
    
    # Use gpg --full-generate-key
    gpg_cmd = [GPG_BIN, "--full-generate-key"]
    print(f"Executing: {' '.join(gpg_cmd)}")
    try:
        # This will be highly interactive in the console
        subprocess.run(gpg_cmd, check=False)
        print("✅ GPG key creation sequence completed. REMEMBER TO SET SIGNINGKEY IN GIT CONFIG.")
    except Exception as e:
        print(f"❌ Error running gpg: {e}", file=sys.stderr)

def import_keys_ssh_gpg():
    """Prompts for a folder and imports keys from it."""
    print("\n--- Key Import ---")
    folder = input("Enter the full path to the folder containing keys to import: ").strip()
    folder_path = Path(folder)
    
    if folder_path.exists() and folder_path.is_dir():
        # Import GPG keys
        print("Importing GPG keys...")
        for key_file in folder_path.glob("*.asc"):
            try:
                subprocess.run([GPG_BIN, "--import", str(key_file)], check=True, shell=True)
                print(f"  + Imported {key_file.name}")
            except subprocess.CalledProcessError:
                print(f"  ❌ Failed to import {key_file.name}")
        
        print("\nREMINDER: You must manually set your signing key and enable signing:")
        print("  git config --global user.signingkey <YOUR KEY ID>")
        print("  git config --global commit.gpgsign true")
    else:
        print(f"❌ Folder not found: {folder_path}", file=sys.stderr)

def main():
    if not GIT_BIN:
        print("❌ Git is required and not found on your system PATH.", file=sys.stderr)
        sys.exit(1)
        
    if not check_admin():
        print("⚠️ Warning: Running some commands (like installing software) may require Administrator privileges.")
        
    print("Welcome to Git/GnuPG/SSH Setup.")
    
    if input("Do you want to proceed with setup? (y/n): ").lower() != 'y':
        print("Aborting.")
        return

    initialize_git_user()
    enable_ssh_and_gpg_agent()
    
    key_mode = input("Are you creating [N]ew keys or [I]mporting existing keys? (n/i): ").lower()
    
    if key_mode == 'n':
        set_ssh_key()
        set_gpg_key()
    elif key_mode == 'i':
        import_keys_ssh_gpg()
    else:
        print("Invalid choice. Aborting key setup.")

if __name__ == "__main__":
    main()