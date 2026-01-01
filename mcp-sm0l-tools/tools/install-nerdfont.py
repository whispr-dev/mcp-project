
import subprocess
import sys
import os
from pathlib import Path
import requests # Assuming 'requests' is installed

def download_latest_github_asset(repo, file_like, output_path):
    """Downloads a file from the latest GitHub release of a given repository."""
    api_url = f"https://api.github.com/repos/{repo}/releases/latest"
    
    try:
        response = requests.get(api_url, timeout=15).json()
        asset_url = next(
            asset["browser_download_url"] 
            for asset in response.get("assets", []) 
            if file_like in asset["name"]
        )
        
        print(f"Downloading {asset_url}...")
        file_response = requests.get(asset_url, stream=True)
        file_response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in file_response.iter_content(chunk_size=8192):
                f.write(chunk)
        return output_path
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading asset: {e}", file=sys.stderr)
        return None
    except StopIteration:
        print(f"❌ Error: Could not find asset matching '{file_like}' in release.", file=sys.stderr)
        return None

def install_archwsl():
    """Installs ArchWSL using the AppX package and certificate."""
    
    temp_dir = Path(os.environ.get("TEMP", "."))
    
    # 1. Download and install certificate
    print("Installing ArchWSL Certificate...")
    cert_path = download_latest_github_asset("yuk7/ArchWSL", ".cer", temp_dir / "ArchWSL.cer")
    if cert_path:
        try:
            # certutil.exe -addstore "Root" ArchWSL.cer
            subprocess.run(["certutil.exe", "-addstore", "Root", str(cert_path)], check=True, shell=True)
            print("✅ Certificate installed.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing certificate (Requires Admin): {e}", file=sys.stderr)

    # 2. Download and install AppX package
    print("Installing ArchWSL AppX package...")
    appx_path = download_latest_github_asset("yuk7/ArchWSL", ".appx", temp_dir / "ArchWSL.appx")
    if appx_path:
        try:
            # Add-AppxPackage -Path ArchWSL.appx
            # We must use PowerShell's cmdlet here as there's no native .exe for this
            subprocess.run(
                ["powershell", "-Command", f"Add-AppxPackage -Path '{str(appx_path)}'"], 
                check=True, shell=True
            )
            print("✅ ArchWSL installed.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error installing AppX (Requires Admin): {e}", file=sys.stderr)

if __name__ == "__main__":
    install_archwsl()