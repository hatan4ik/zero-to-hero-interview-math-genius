#!/bin/bash
# GitHub Actions History Cleaner - Bash Version
# Requires: curl, jq, GITHUB_TOKEN environment variable

REPO_OWNER="hatan4ik"
REPO_NAME="zero-to-hero-interview-math-genius"

if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Error: GITHUB_TOKEN environment variable not set"
    echo "Generate token at: https://github.com/settings/tokens"
    echo "Required scopes: repo, actions"
    exit 1
fi

echo "🧹 GitHub Actions History Cleaner"
echo "=================================="

# Get all workflow runs
echo "📋 Fetching workflow runs..."
RUNS=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
    -H "Accept: application/vnd.github.v3+json" \
    "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/runs" | \
    jq -r '.workflow_runs[].id')

if [ -z "$RUNS" ]; then
    echo "✅ No workflow runs found!"
    exit 0
fi

# Count runs
RUN_COUNT=$(echo "$RUNS" | wc -l)
echo "📊 Found $RUN_COUNT workflow runs to delete"

# Delete each run
DELETED=0
FAILED=0
COUNTER=1

for RUN_ID in $RUNS; do
    echo "🗑️  [$COUNTER/$RUN_COUNT] Deleting run ID: $RUN_ID"
    
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
        -X DELETE \
        -H "Authorization: token $GITHUB_TOKEN" \
        -H "Accept: application/vnd.github.v3+json" \
        "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/actions/runs/$RUN_ID")
    
    if [ "$HTTP_CODE" = "204" ]; then
        echo "   ✅ Deleted successfully"
        ((DELETED++))
    else
        echo "   ❌ Failed (HTTP $HTTP_CODE)"
        ((FAILED++))
    fi
    
    ((COUNTER++))
    sleep 0.1  # Rate limiting
done

echo ""
echo "=================================="
echo "📊 Summary:"
echo "   ✅ Deleted: $DELETED"
echo "   ❌ Failed: $FAILED"
echo "   📋 Total: $RUN_COUNT"

if [ $DELETED -gt 0 ]; then
    echo ""
    echo "🎉 Actions history cleaned successfully!"
else
    echo ""
    echo "⚠️  No actions were deleted. Check your token permissions."
fi