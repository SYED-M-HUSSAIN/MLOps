import requests
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import os
import requests

def fetch_pr_diff(env):
    diff_url = f"https://api.github.com/repos/{env['repo_owner']}/{env['repo_name']}/pulls/{env['pr_number']}"
    headers = {
        "Authorization": f"token {env['github_token']}",
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(diff_url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch PR diff: {response.status_code} - {response.text}")

    return response.text
