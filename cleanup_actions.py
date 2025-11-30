#!/usr/bin/env python3
"""
GitHub Actions History Cleaner
Deletes all workflow runs from a repository using GitHub API
"""

import requests
import json
import time
import os

# Configuration
REPO_OWNER = "hatan4ik"
REPO_NAME = "zero-to-hero-interview-math-genius"
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Set this environment variable

if not GITHUB_TOKEN:
    print("❌ Error: GITHUB_TOKEN environment variable not set")
    print("Generate token at: https://github.com/settings/tokens")
    print("Required scopes: repo, actions")
    exit(1)

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_workflow_runs():
    """Get all workflow runs"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()["workflow_runs"]
    else:
        print(f"❌ Failed to get workflow runs: {response.status_code}")
        return []

def delete_workflow_run(run_id):
    """Delete a specific workflow run"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/runs/{run_id}"
    response = requests.delete(url, headers=headers)
    return response.status_code == 204

def main():
    print("🧹 GitHub Actions History Cleaner")
    print("=" * 40)
    
    # Get all workflow runs
    print("📋 Fetching workflow runs...")
    runs = get_workflow_runs()
    
    if not runs:
        print("✅ No workflow runs found!")
        return
    
    print(f"📊 Found {len(runs)} workflow runs to delete")
    
    # Delete each run
    deleted = 0
    failed = 0
    
    for i, run in enumerate(runs, 1):
        run_id = run["id"]
        run_name = run["name"]
        
        print(f"🗑️  [{i}/{len(runs)}] Deleting: {run_name} (ID: {run_id})")
        
        if delete_workflow_run(run_id):
            deleted += 1
            print(f"   ✅ Deleted successfully")
        else:
            failed += 1
            print(f"   ❌ Failed to delete")
        
        # Rate limiting - GitHub allows 5000 requests/hour
        time.sleep(0.1)
    
    print("\n" + "=" * 40)
    print(f"📊 Summary:")
    print(f"   ✅ Deleted: {deleted}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📋 Total: {len(runs)}")
    
    if deleted > 0:
        print("\n🎉 Actions history cleaned successfully!")
    else:
        print("\n⚠️  No actions were deleted. Check your token permissions.")

if __name__ == "__main__":
    main()