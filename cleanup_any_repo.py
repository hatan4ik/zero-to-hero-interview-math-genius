#!/usr/bin/env python3
import requests
import os
import subprocess
import sys

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
    
    print("GitHub token not found. Please enter your token:")
    return input("Token: ").strip()

def get_public_repos(username, token):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [repo for repo in response.json() if not repo["private"]]
    return []

def cleanup_repo_actions(owner, repo_name, token):
    headers = {"Authorization": f"token {token}"}
    
    # Get workflow runs
    url = f"https://api.github.com/repos/{owner}/{repo_name}/actions/runs"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to get runs for {repo_name}")
        return
    
    runs = response.json()["workflow_runs"]
    if not runs:
        print(f"✅ {repo_name}: No workflow runs")
        return
    
    print(f"🗑️ {repo_name}: Deleting {len(runs)} runs...")
    
    # Delete runs
    for run in runs:
        delete_url = f"https://api.github.com/repos/{owner}/{repo_name}/actions/runs/{run['id']}"
        requests.delete(delete_url, headers=headers)
    
    print(f"✅ {repo_name}: Cleaned!")

def main():
    username = "hatan4ik"
    token = get_github_token()
    
    print(f"📋 Getting public repos for {username}...")
    repos = get_public_repos(username, token)
    
    if not repos:
        print("❌ No public repos found")
        return
    
    print(f"\n📊 Found {len(repos)} public repos:")
    for i, repo in enumerate(repos, 1):
        print(f"{i:2d}. {repo['name']}")
    
    print("\n🧹 Cleaning Actions history from all repos...")
    for repo in repos:
        cleanup_repo_actions(username, repo["name"], token)
    
    print("\n🎉 All repos cleaned!")

if __name__ == "__main__":
    main()