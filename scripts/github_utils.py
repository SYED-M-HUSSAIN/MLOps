from github import Github
import requests
from .config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME, PR_NUMBER

g = Github(GITHUB_TOKEN)
repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

def fetch_pr_diff():
    pr = repo.get_pull(PR_NUMBER)
    diff_url = pr.diff_url
    print(f"Fetched Diff URL: {diff_url}")

    diff_response = requests.get(diff_url, headers={
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    })

    diff_text = diff_response.text
    print(f"Fetched Diff Text: {diff_text[:1000]}...")
    return diff_text

def post_review_comment(review_comment):
    pr = repo.get_pull(PR_NUMBER)
    pr.create_issue_comment(f"🤖 AI Code Review (via Claude):\n\n{review_comment}")
    print("Review comment posted successfully.")
