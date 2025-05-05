from .github_utils import fetch_pr_diff, post_review_comment
from .anthropic_utils import call_anthropic_api

def run_review():
    diff_text = fetch_pr_diff()
    review_comment = call_anthropic_api(diff_text)
    print(f"Received Review Comment: {review_comment[:1000]}...")
    post_review_comment(review_comment)
