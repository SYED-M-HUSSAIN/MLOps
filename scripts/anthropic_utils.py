import requests
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from .config import ANTHROPIC_API_KEY
from scripts.utils import load_criteria  # assuming you use markdown criteria

def call_anthropic_api(diff_text):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }

    # Load system-level evaluation instructions
    system_prompt = load_criteria("evaluation_criteria/code_quality.md") 

    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1000,
        "temperature": 0.2,
        "system": system_prompt,
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Here is the code diff for review:\n\n{diff_text}\n\n"
                    "Please analyze this code and share your feedback."
                )
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Anthropic API error: {response.status_code} - {response.text}")

    data = response.json()
    if "content" not in data:
        raise Exception(f"Malformed Anthropic response: {data}")

    return data["content"][0]["text"]
