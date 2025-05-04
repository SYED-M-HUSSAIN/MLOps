import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def load_template(template_name: str = "default") -> str:
    base_path = os.path.join(os.path.dirname(__file__), "../custom_evaluations")
    template_file = os.path.join(base_path, f"{template_name}.md")

    try:
        with open(template_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ Template {template_name} not found. Proceeding without it.")
        return ""
