#!/usr/bin/env python3
"""
GitHub Repo Syncer - Keep GitHub repos synced across machines
Requires: pip install requests
"""
import argparse
import subprocess
from pathlib import Path
try:
    import requests
except ImportError:
    print("Please install: pip install requests")
    exit(1)

def sync_github_repos(username: str, token: str = None, target_dir: str = "repos"):
    """Clone and update all user's GitHub repos"""
    target_path = Path(target_dir)
    target_path.mkdir(exist_ok=True)
    
    headers = {}
    if token:
        headers["Authorization"] = f"token {token}"
    
    print(f"📦 Syncing GitHub repos for @{username}")
    print(f"   Target directory: {target_path.resolve()}\n")
    
    try:
        # Get all repos
        repos = requests.get(
            f"https://api.github.com/users/{username}/repos",
            headers=headers
        ).json()
        
        if not isinstance(repos, list):
            print("Error: Unable to fetch repositories. Check username/token.")
            return
        
        print(f"Found {len(repos)} repositories\n")
        
        cloned = 0
        updated = 0
        errors = 0
        
        for repo in repos:
            name = repo["name"]
            clone_url = repo["clone_url"]
            repo_path = target_path / name
            
            if not repo_path.exists():
                # Clone new repo
                try:
                    subprocess.run(["git", "clone", clone_url], 
                                 cwd=target_path, check=True,
                                 stdout=subprocess.DEVNULL, 
                                 stderr=subprocess.DEVNULL)
                    print(f"✓ Cloned: {name}")
                    cloned += 1
                except subprocess.CalledProcessError:
                    print(f"✗ Failed to clone: {name}")
                    errors += 1
            else:
                # Update existing repo
                try:
                    subprocess.run(["git", "-C", str(repo_path), "pull"], 
                                 check=True,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
                    print(f"↻ Updated: {name}")
                    updated += 1
                except subprocess.CalledProcessError:
                    print(f"✗ Failed to update: {name}")
                    errors += 1
        
        print(f"\n{'='*50}")
        print(f"Cloned: {cloned} | Updated: {updated} | Errors: {errors}")
        
    except requests.RequestException as e:
        print(f"Error: Unable to connect to GitHub API. {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync GitHub repositories")
    parser.add_argument("username", help="GitHub username")
    parser.add_argument("-t", "--token", help="GitHub personal access token (optional)")
    parser.add_argument("-d", "--dir", default="repos", help="Target directory")
    
    args = parser.parse_args()
    sync_github_repos(args.username, args.token, args.dir)
