from github import Github
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))


def get_repo(env):
    g = Github(env["github_token"])
    return g.get_repo(f"{env['repo_owner']}/{env['repo_name']}")

def post_review_comment(repo, pr_number, review_comment):
    pr = repo.get_pull(pr_number)
    pr.create_issue_comment(f"🤖 AI Code Review (via Claude):\n\n{review_comment}")
