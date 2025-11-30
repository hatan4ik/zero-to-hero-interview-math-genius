#!/usr/bin/env python3
import os
import subprocess
import sys
from datetime import datetime

import requests

API_ROOT = "https://api.github.com"
OWNER = "hatan4ik"
TAG_NAME = "last"
RELEASE_NAME = "last"


def get_github_token():
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token

    try:
        result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except FileNotFoundError:
        pass

    print("GitHub token not found. Please enter a token with 'public_repo' or 'repo' scope.")
    return input("Token: ").strip()


def auth_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }


def get_public_repos(username, token):
    headers = auth_headers(token)
    repos = []
    page = 1

    while True:
        response = requests.get(
            f"{API_ROOT}/users/{username}/repos",
            headers=headers,
            params={"type": "public", "per_page": 100, "page": page, "sort": "pushed"},
            timeout=30,
        )

        if response.status_code != 200:
            print(f"❌ Failed to fetch repos (status {response.status_code})")
            print(response.text)
            break

        batch = response.json()
        if not batch:
            break

        repos.extend(batch)
        page += 1

    return repos


def get_branch_head(owner, repo, branch, token):
    response = requests.get(
        f"{API_ROOT}/repos/{owner}/{repo}/commits/{branch}",
        headers=auth_headers(token),
        timeout=30,
    )
    if response.status_code == 200:
        return response.json().get("sha")

    print(f"❌ {repo}: Failed to get head for {branch} (status {response.status_code})")
    return None


def ensure_tag(owner, repo, tag_name, target_sha, token):
    headers = auth_headers(token)
    create_response = requests.post(
        f"{API_ROOT}/repos/{owner}/{repo}/git/refs",
        headers=headers,
        json={"ref": f"refs/tags/{tag_name}", "sha": target_sha},
        timeout=30,
    )

    if create_response.status_code == 201:
        return "created"

    if create_response.status_code != 422:
        print(f"❌ {repo}: Failed to create tag ({create_response.status_code})")
        print(create_response.text)
        return None

    update_response = requests.patch(
        f"{API_ROOT}/repos/{owner}/{repo}/git/refs/tags/{tag_name}",
        headers=headers,
        json={"sha": target_sha, "force": True},
        timeout=30,
    )

    if update_response.status_code in (200, 201):
        return "updated"

    print(f"❌ {repo}: Failed to update tag ({update_response.status_code})")
    print(update_response.text)
    return None


def ensure_release(owner, repo, tag_name, branch, target_sha, token):
    headers = auth_headers(token)
    release_body = (
        f"Automated '{RELEASE_NAME}' release from {branch} @ {target_sha[:7]} "
        f"on {datetime.utcnow().isoformat()}Z."
    )

    existing_response = requests.get(
        f"{API_ROOT}/repos/{owner}/{repo}/releases/tags/{tag_name}",
        headers=headers,
        timeout=30,
    )

    if existing_response.status_code == 200:
        release_id = existing_response.json()["id"]
        update_response = requests.patch(
            f"{API_ROOT}/repos/{owner}/{repo}/releases/{release_id}",
            headers=headers,
            json={
                "tag_name": tag_name,
                "target_commitish": branch,
                "name": RELEASE_NAME,
                "body": release_body,
                "draft": False,
                "prerelease": False,
                "make_latest": "true",
            },
            timeout=30,
        )
        if update_response.status_code in (200, 201):
            return "updated"

        print(f"❌ {repo}: Failed to update release ({update_response.status_code})")
        print(update_response.text)
        return None

    if existing_response.status_code != 404:
        print(f"❌ {repo}: Failed to check existing release ({existing_response.status_code})")
        print(existing_response.text)
        return None

    create_response = requests.post(
        f"{API_ROOT}/repos/{owner}/{repo}/releases",
        headers=headers,
        json={
            "tag_name": tag_name,
            "target_commitish": branch,
            "name": RELEASE_NAME,
            "body": release_body,
            "draft": False,
            "prerelease": False,
            "make_latest": "true",
        },
        timeout=30,
    )

    if create_response.status_code == 201:
        return "created"

    print(f"❌ {repo}: Failed to create release ({create_response.status_code})")
    print(create_response.text)
    return None


def main():
    token = get_github_token()
    if not token:
        print("❌ No token provided. Exiting.")
        sys.exit(1)

    print(f"📋 Fetching public repos for {OWNER}...")
    repos = get_public_repos(OWNER, token)

    if not repos:
        print("❌ No public repos found or fetch failed.")
        sys.exit(1)

    print(f"📊 Found {len(repos)} public repos")
    for repo in repos:
        name = repo["name"]
        if repo.get("archived") or repo.get("disabled"):
            print(f"⚠️  {name}: Skipped (archived or disabled)")
            continue

        branch = repo.get("default_branch") or "main"
        head_sha = get_branch_head(OWNER, name, branch, token)
        if not head_sha:
            continue

        tag_result = ensure_tag(OWNER, name, TAG_NAME, head_sha, token)
        if not tag_result:
            continue

        release_result = ensure_release(OWNER, name, TAG_NAME, branch, head_sha, token)
        if not release_result:
            continue

        print(f"✅ {name}: tag '{TAG_NAME}' {tag_result}, release '{RELEASE_NAME}' {release_result}")

    print("\n🎉 Done.")


if __name__ == "__main__":
    main()
