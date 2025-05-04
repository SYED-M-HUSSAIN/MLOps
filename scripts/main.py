from github_utils import fetch_pr_diff
from anthropic_utils import call_anthropic_api
from comment_utils import post_review_comment

# Main function
def main():
    try:
        # Step 1: Fetch PR diff
        diff_text = fetch_pr_diff()

        # Step 2: Call Anthropic API for review
        review_comment = call_anthropic_api(diff_text)
        print(f"Received Review Comment: {review_comment[:1000]}...")  # Debugging first 1000 chars

        # Step 3: Post review comment on PR
        post_review_comment(review_comment)
        
    except Exception as e:
        print(f"Error: {e}")
        raise e

if __name__ == "__main__":
    main()
