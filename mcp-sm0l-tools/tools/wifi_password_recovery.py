#!/usr/bin/env python3
"""
WiFi Password Recovery - Recover saved WiFi passwords (Windows)
"""
import subprocess
import re
import argparse

def get_saved_wifi_passwords():
    """Recover all saved WiFi passwords from Windows"""
    try:
        # Get list of all saved WiFi profiles
        output = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
        profiles = re.findall(r"All User Profile\s+:\s+(.*)", output)
        
        print(f"Found {len(profiles)} saved WiFi networks\n")
        print(f"{'Network Name':<30} {'Password':<20}")
        print("="*50)
        
        for profile in profiles:
            profile = profile.strip()
            try:
                # Get password for each profile
                result = subprocess.check_output(
                    f'netsh wlan show profile name="{profile}" key=clear', 
                    shell=True
                ).decode()
                
                password = re.search(r"Key Content\s+:\s+(.*)", result)
                
                if password:
                    print(f"{profile:<30} {password.group(1):<20}")
                else:
                    print(f"{profile:<30} {'[No password]':<20}")
                    
            except subprocess.CalledProcessError:
                print(f"{profile:<30} {'[Error]':<20}")
                
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to retrieve WiFi profiles. {e}")
        print("Note: This script requires Windows and may need administrator privileges.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recover saved WiFi passwords (Windows only)")
    args = parser.parse_args()
    
    print("WiFi Password Recovery Tool\n")
    get_saved_wifi_passwords()
