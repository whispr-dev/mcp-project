import subprocess
import sys

def optimize_ssd():
    """
    Optimizes SSD life by disabling last access time logging and
    disabling paging file encryption via fsutil.
    Requires Administrator privileges.
    """
    try:
        # Disable Last Access Time (improves I/O performance and SSD life)
        subprocess.run(["fsutil", "behavior", "set", "DisableLastAccess", "1"], check=True, shell=True)
        print("✅ Disabled file LastAccessTime logging.")
        
        # Disable Paging File Encryption (reduces I/O load)
        subprocess.run(["fsutil", "behavior", "set", "EncryptPagingFile", "0"], check=True, shell=True)
        print("✅ Disabled paging file encryption.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error optimizing SSD (Requires Admin): {e}", file=sys.stderr)
    except FileNotFoundError:
        print("❌ Error: 'fsutil' command not found. Ensure it's on your PATH.", file=sys.stderr)

if __name__ == "__main__":
    optimize_ssd()