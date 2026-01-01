#!/usr/bin/env python3
"""
Image Downloader - Download images from URLs
Requires: pip install requests
"""
import argparse
from pathlib import Path
try:
    import requests
except ImportError:
    print("Please install: pip install requests")
    exit(1)

def download_images(url_file: str, output_dir: str = "downloads"):
    """Download images from list of URLs"""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    with open(url_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    
    print(f"Downloading {len(urls)} images to {output_dir}/\n")
    
    for idx, url in enumerate(urls, 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            # Get filename from URL or use index
            filename = url.split('/')[-1] or f"image_{idx}.jpg"
            filepath = output_path / filename
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"[{idx}/{len(urls)}] Downloaded: {filename}")
            
        except requests.RequestException as e:
            print(f"[{idx}/{len(urls)}] Failed: {url} - {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images from URL list")
    parser.add_argument("url_file", help="Text file with image URLs (one per line)")
    parser.add_argument("-o", "--output", default="downloads", help="Output directory")
    
    args = parser.parse_args()
    download_images(args.url_file, args.output)
