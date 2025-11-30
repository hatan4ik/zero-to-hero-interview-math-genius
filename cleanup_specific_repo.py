#!/usr/bin/env python3
import requests
import os
import subprocess
import sys
import time

def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token
    
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    
    return input("Token: ").strip()

def cleanup_repo(owner, repo_name, token):
    headers = {"Authorization": f"token {token}"}
    
    while True:
        # Get workflow runs
        url = f"https://api.github.com/repos/{owner}/{repo_name}/actions/runs"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to get runs: {response.status_code}")
            break
        
        runs = response.json()["workflow_runs"]
        if not runs:
            print("✅ No more workflow runs!")
            break
        
        print(f"🗑️ Deleting {len(runs)} runs...")
        
        # Delete runs
        for run in runs:
            delete_url = f"https://api.github.com/repos/{owner}/{repo_name}/actions/runs/{run['id']}"
            result = requests.delete(delete_url, headers=headers)
            print(f"   Run {run['id']}: {'✅' if result.status_code == 204 else '❌'}")
            time.sleep(0.1)
        
        print(f"Batch complete. Checking for more...")

def main():
    owner = "hatan4ik"
    repo_name = "Top-10-CI-CD-SecurityRisks"
    token = get_github_token()
    
    print(f"🧹 Cleaning {owner}/{repo_name}...")
    cleanup_repo(owner, repo_name, token)
    print("🎉 Done!")

if __name__ == "__main__":
    main()