from github import Github
from config import GITHUB_TOKEN, REPO_OWNER, REPO_NAME, PR_NUMBER

# GitHub Setup
g = Github(GITHUB_TOKEN)
repo = g.get_repo(f"{REPO_OWNER}/{REPO_NAME}")

# Step 3: Post Review Comment on PR
def post_review_comment(review_comment):
    pr = repo.get_pull(PR_NUMBER)
    pr.create_issue_comment(f"🤖 AI Code Review (via Claude):\n\n{review_comment}")
    print("Review comment posted successfully.")
