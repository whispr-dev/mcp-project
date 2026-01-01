#!/usr/bin/env python3
"""
Page Monitor - Monitor webpage for changes
Requires: pip install requests
"""
import argparse
import hashlib
from pathlib import Path
try:
    import requests
except ImportError:
    print("Please install: pip install requests")
    exit(1)

def get_page_hash(url: str) -> str:
    """Get MD5 hash of page content"""
    response = requests.get(url, timeout=10)
    return hashlib.md5(response.content).hexdigest()

def monitor_page(url: str):
    """Check if page has changed since last check"""
    cache_file = Path(".page_monitor_cache")
    cache = {}
    
    # Load cache
    if cache_file.exists():
        with open(cache_file, 'r') as f:
            for line in f:
                cached_url, cached_hash = line.strip().split('|', 1)
                cache[cached_url] = cached_hash
    
    try:
        current_hash = get_page_hash(url)
        
        if url in cache:
            if cache[url] != current_hash:
                print(f"🔔 CHANGED: {url}")
                print(f"   Old hash: {cache[url]}")
                print(f"   New hash: {current_hash}")
            else:
                print(f"✓ No change: {url}")
        else:
            print(f"📌 First check: {url}")
            print(f"   Hash: {current_hash}")
        
        # Update cache
        cache[url] = current_hash
        with open(cache_file, 'w') as f:
            for cached_url, cached_hash in cache.items():
                f.write(f"{cached_url}|{cached_hash}\n")
                
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monitor webpage for changes")
    parser.add_argument("url", help="URL to monitor")
    
    args = parser.parse_args()
    monitor_page(args.url)
