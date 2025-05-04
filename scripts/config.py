import os
import sys


# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))


class Config:
    GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    REPO_OWNER = os.getenv("REPO_OWNER")
    REPO_NAME = os.getenv("REPO_NAME")
    PR_NUMBER = int(os.getenv("PR_NUMBER", 0))
