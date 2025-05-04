from scripts.config import Config
from scripts.github_client import get_repo, post_review_comment
from scripts.diff_fetcher import fetch_pr_diff
from scripts.anthropic_client import call_anthropic_api
from scripts.reviewer import load_template


def main():
    try:
        repo = get_repo()
        diff_text = fetch_pr_diff(repo)

        template = load_template("default")  # Change to "security", etc. as needed

        review_comment = call_anthropic_api(diff_text, template)
        post_review_comment(repo.get_pull(Config.PR_NUMBER), review_comment)

    except Exception as e:
        print(f"❌ Error occurred: {e}")
        raise
