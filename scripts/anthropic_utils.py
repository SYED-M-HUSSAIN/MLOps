import requests
from .config import ANTHROPIC_API_KEY

def call_anthropic_api(diff_text):
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01"
    }

    payload = {
        "model": "claude-3-7-sonnet-20250219",
        "max_tokens": 1000,
        "temperature": 0.2,
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Review the following code changes:\n{diff_text}\n"
                    "Please provide feedback on code quality, readability, bugs, and optimization opportunities."
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
