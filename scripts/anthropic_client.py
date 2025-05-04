import requests
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.config import Config


def call_anthropic_api(diff_text: str, template: str = None) -> str:
    prompt = f"Review the following code changes:\n{diff_text}\n"
    if template:
        prompt += f"\nAdditional Review Context:\n{template}\n"

    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1000,
        "temperature": 0.2,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-key": Config.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }

    print("📡 Sending request to Anthropic API...")
    response = requests.post("https://api.anthropic.com/v1/messages", json=payload, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Anthropic API error: {response.status_code} - {response.text}")

    data = response.json()
    return data["content"][0]["text"]
