from scripts.reviewer import run_review

if __name__ == "__main__":
    try:
        run_review()
    except Exception as e:
        print(f"Error: {e}")
        raise
