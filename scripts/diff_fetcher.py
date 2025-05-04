import requests
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def fetch_pr_diff(repo, pr_number):
    pr = repo.get_pull(pr_number)
    diff_url = pr.diff_url

    response = requests.get(diff_url, headers={
        "Authorization": f"token {repo._requester._AuthorizationHeader}",
        "Accept": "application/vnd.github.v3.diff"
    })

    if response.status_code != 200:
        raise Exception(f"Failed to fetch PR diff: {response.status_code}")

    return response.text
