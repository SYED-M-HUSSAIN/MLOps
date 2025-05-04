import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import os

def load_env_variables():
    return {
        "github_token": os.getenv("GITHUB_TOKEN"),
        "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
        "repo_owner": os.getenv("REPO_OWNER"),
        "repo_name": os.getenv("REPO_NAME"),
        "pr_number": int(os.getenv("PR_NUMBER")),
    }
