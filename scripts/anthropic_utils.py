import requests
from config import ANTHROPIC_API_KEY
import os

def call_anthropic_api(diff_text):
    # Load template prompt from file
    prompt_path = os.path.join(os.path.dirname(__file__), '..', 'evaluation_criteria', 'review_prompt.txt')
    with open(prompt_path, 'r') as file:
        template_prompt = file.read()

    full_prompt = template_prompt.replace("{{diff}}", diff_text)

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
                "content": full_prompt
            }
        ]
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise Exception(f"Failed to call Anthropic API: {response.status_code} - {response.text}")
    
    data = response.json()
    if "content" not in data:
        raise Exception(f"Anthropic API error: {data}")
    
    return data["content"][0]["text"]
