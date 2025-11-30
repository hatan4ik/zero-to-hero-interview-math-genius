#!/usr/bin/env python3
import os
import subprocess
import sys

def get_github_token():
    """Get GitHub token from various sources"""
    
    # Check environment variable
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token
    
    # Check gh CLI
    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    
    # Check git config
    try:
        result = subprocess.run(["git", "config", "--global", "github.token"], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    
    # Manual input
    print("GitHub token not found. Please enter your token:")
    print("Generate at: https://github.com/settings/tokens")
    print("Required scopes: repo, actions")
    return input("Token: ").strip()

def main():
    token = get_github_token()
    if not token:
        print("❌ No token provided")
        sys.exit(1)
    
    # Set environment variable and run cleanup
    env = os.environ.copy()
    env["GITHUB_TOKEN"] = token
    
    subprocess.run([sys.executable, "cleanup_actions.py"], env=env)

if __name__ == "__main__":
    main()