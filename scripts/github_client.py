from github import Github
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from scripts.config import Config


def get_repo():
    g = Github(Config.GITHUB_TOKEN)
    return g.get_repo(f"{Config.REPO_OWNER}/{Config.REPO_NAME}")


def get_pull_request(repo):
    return repo.get_pull(Config.PR_NUMBER)


def post_review_comment(pr, comment: str):
    pr.create_issue_comment(f"🤖 AI Code Review (via Claude):\n\n{comment}")
    print("✅ Review comment posted successfully.")
