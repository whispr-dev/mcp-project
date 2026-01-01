#!/usr/bin/env python3
"""
Incremental Backup - Only backup files that changed since last backup
"""
import shutil
import argparse
import hashlib
import json
from pathlib import Path
from datetime import datetime

def file_hash(filepath):
    """Calculate file hash"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def incremental_backup(source: str, dest: str):
    """Backup only changed files"""
    source_path = Path(source)
    dest_path = Path(dest)
    dest_path.mkdir(parents=True, exist_ok=True)
    
    cache_file = dest_path / ".backup_cache.json"
    cache = {}
    
    # Load cache
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            cache = json.load(f)
    
    backed_up = 0
    skipped = 0
    
    for file in source_path.rglob("*"):
        if file.is_file():
            rel_path = str(file.relative_to(source_path))
            current_hash = file_hash(file)
            
            # Check if changed
            if rel_path not in cache or cache[rel_path] != current_hash:
                dest_file = dest_path / rel_path
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, dest_file)
                cache[rel_path] = current_hash
                print(f"✓ Backed up: {rel_path}")
                backed_up += 1
            else:
                skipped += 1
    
    # Save cache
    with open(cache_file, 'w') as f:
        json.dump(cache, f)
    
    print(f"\nBacked up: {backed_up} files")
    print(f"Skipped (unchanged): {skipped} files")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Incremental backup")
    parser.add_argument("source", help="Source directory")
    parser.add_argument("dest", help="Backup destination")
    
    args = parser.parse_args()
    incremental_backup(args.source, args.dest)
