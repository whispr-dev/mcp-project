#!/usr/bin/env python3
"""
Process Monitor & Auto-Restart - Monitor and restart processes
Requires: pip install psutil
"""
import argparse
import subprocess
import time
try:
    import psutil
except ImportError:
    print("Please install: pip install psutil")
    exit(1)

def is_running(process_name: str) -> bool:
    """Check if process is running"""
    for proc in psutil.process_iter(['name']):
        try:
            if process_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False

def monitor_and_restart(command: str, check_interval: int = 30):
    """Monitor process and restart if it crashes"""
    process_name = command.split()[0]
    
    print(f"🔍 Process Monitor started")
    print(f"   Command: {command}")
    print(f"   Check interval: {check_interval} seconds")
    print("Press Ctrl+C to stop\n")
    
    restarts = 0
    
    try:
        while True:
            if not is_running(process_name):
                print(f"⚠️  Process '{process_name}' not running. Restarting...")
                try:
                    subprocess.Popen(command.split())
                    restarts += 1
                    print(f"✓ Restarted (#{restarts})")
                except Exception as e:
                    print(f"✗ Failed to restart: {e}")
            
            time.sleep(check_interval)
            
    except KeyboardInterrupt:
        print(f"\n\nMonitoring stopped. Total restarts: {restarts}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor and auto-restart processes")
    parser.add_argument("command", help="Command to monitor and restart")
    parser.add_argument("-i", "--interval", type=int, default=30,
                       help="Check interval in seconds (default: 30)")
    
    args = parser.parse_args()
    monitor_and_restart(args.command, args.interval)
