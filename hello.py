import os
import requests
from github import Github

# Constants
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
REPO_OWNER = os.getenv('REPO_OWNER')
REPO_NAME = os.getenv('REPO_NAME')
PR_NUMBER = os.getenv('PR_NUMBER')

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

# Step 2: Call Anthropic API (Claude) for Review
def call_anthropic_api(diff_text):
    url = "https://api.anthropic.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ANTHROPIC_API_KEY}"
    }
    
    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "prompt": f"Review the following code changes:\n{diff_text}\nPlease provide feedback on code quality, readability, bugs, and optimization opportunities.",
        "max_tokens": 1000,
        "temperature": 0.2
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to call Anthropic API: {response.status_code} - {response.text}")
    
    data = response.json()
    if "completion" not in data:
        raise Exception(f"Anthropic API error: {data}")
    
    return data["completion"]

# Step 3: Post Review Comment on PR
def post_review_comment(review_comment):
    pr = repo.get_pull(PR_NUMBER)
    pr.create_issue_comment(f"🤖 AI Code Review (via Claude):\n\n{review_comment}")
    print("Review comment posted successfully.")

# Main function
def main():
    try:
        # Step 1: Fetch PR diff
        diff_text = fetch_pr_diff()

        # Step 2: Call Anthropic API for review
        review_comment = call_anthropic_api(diff_text)
        print(f"Received Review Comment: {review_comment[:1000]}...")  # Debugging first 1000 chars

        # Step 3: Post review comment on PR
        post_review_comment(review_comment)
        
    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == "__main__":
    main()
