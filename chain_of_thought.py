import requests
from dotenv import load_dotenv
import json
import os

load_dotenv()

OPENROUTER_API_KEY= os.getenv("OPENROUTER_API_KEY")


MODEL = "openai/gpt-4o-mini"  

url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

messages = [
    {
        "role": "system",
        "content": (
            """
            You are a problem-solving assistant.
            Think internally but expose only explicit user-facing steps.
            Return ONE step at a time in JSON.
            With each step mention that in a separate key with a value
            You MUST return valid JSON only.
            NO extra text.
            NO explanations outside JSON.

            Allowed keys ONLY:
            - step (number)
            - content (string)
            - status ("continue" or "done")

            If you violate the format, you are wrong.
            """
        )
    },
    {
        "role": "user",
        "content": (
            "Solve this problem step by step:\n"
            "If a number is multiplied by 3 and then 5 is added, the result is 20.\n"
            "Find the number.\n"
            "Remember: one step per response."
        )
    }
]

all_steps = []

while True:
    payload = {
        "model": MODEL,
        "messages": messages,
        "temperature": 0.2
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    assistant_msg = result["choices"][0]["message"]["content"]

    step_data = json.loads(assistant_msg)
    all_steps.append(step_data)

    print(f"Step {step_data['step']}: {step_data['content']}")

    if step_data["status"] == "done":
        print("\nFinal Answer Reached")
        break

    # Feed model’s last step back into context
    messages.append({
        "role": "assistant",
        "content": assistant_msg
    })
