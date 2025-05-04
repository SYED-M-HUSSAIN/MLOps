import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def apply_custom_evaluation(diff_text, strategy="default"):
    template_path = f"custom_evaluations/{strategy}.md"
    try:
        with open(template_path, "r") as f:
            template = f.read()
    except FileNotFoundError:
        template = "Please review the following code changes:"

    return f"{template}\n\n{diff_text}"
