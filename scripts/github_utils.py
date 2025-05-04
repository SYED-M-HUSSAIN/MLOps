import requests
from github import Github
from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME, PR_NUMBER

# GitHub Setup
g = Github(GITHUB_TOKEN)
repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

# Step 1: Fetch PR Diff
def fetch_pr_diff():
    pr = repo.get_pull(PR_NUMBER)
    diff_url = pr.diff_url
    print(f"Fetched Diff URL: {diff_url}")
    
    diff_response = requests.get(diff_url, headers={
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    })
    
    diff_text = diff_response.text
    print(f"Fetched Diff Text: {diff_text[:1000]}...")  # Debug: first 1000 chars for logging
    return diff_text
