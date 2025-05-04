import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.config import load_env_variables
from scripts.github_client import get_repo, post_review_comment
from scripts.diff_fetcher import fetch_pr_diff
from scripts.anthropic_client import get_review_from_anthropic
from scripts.reviewer import apply_custom_evaluation

def main():
    env = load_env_variables()
    repo = get_repo(env)

    diff_text = fetch_pr_diff(repo, env["pr_number"])
    prompt = apply_custom_evaluation(diff_text, strategy="default")
    review_comment = get_review_from_anthropic(env["anthropic_api_key"], prompt)

    post_review_comment(repo, env["pr_number"], review_comment)

    # This line is necessary for GitHub Action echo
    print(review_comment)

if __name__ == "__main__":
    main()
