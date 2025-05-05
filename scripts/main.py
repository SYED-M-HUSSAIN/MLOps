import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.reviewer import run_review

if __name__ == "__main__":
    try:
        run_review()
    except Exception as e:
        print(f"Error: {e}")
        raise
