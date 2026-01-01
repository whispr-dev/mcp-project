#!/usr/bin/env python3
"""
Simple Backup - Create timestamped backups of directories
"""
import shutil
import argparse
from pathlib import Path
from datetime import datetime

def backup_directory(source: str, dest_root: str = "backups"):
    """Create timestamped backup of directory"""
    source_path = Path(source)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    backup_name = f"{source_path.name}_{timestamp}"
    dest_path = Path(dest_root) / backup_name
    
    print(f"Backing up {source} to {dest_path}...")
    
    try:
        shutil.copytree(source_path, dest_path)
        
        # Calculate size
        total_size = sum(f.stat().st_size for f in dest_path.rglob('*') if f.is_file())
        
        print(f"✓ Backup complete!")
        print(f"  Location: {dest_path}")
        print(f"  Size: {total_size / (1024**2):.2f} MB")
        
    except Exception as e:
        print(f"✗ Backup failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create timestamped backup")
    parser.add_argument("source", help="Directory to backup")
    parser.add_argument("-d", "--dest", default="backups", help="Backup destination")
    
    args = parser.parse_args()
    backup_directory(args.source, args.dest)
