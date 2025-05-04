import requests
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))

from scripts.config import Config
from scripts.github_client import get_pull_request


def fetch_pr_diff(repo):
    pr = get_pull_request(repo)
    diff_url = pr.diff_url
    print(f"📄 Fetching diff from: {diff_url}")

    headers = {
        "Authorization": f"token {Config.GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(diff_url, headers=headers)
    response.raise_for_status()

    diff_text = response.text
    print(f"✅ Diff fetched ({len(diff_text)} characters)")
    return diff_text
