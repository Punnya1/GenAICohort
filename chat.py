from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
) 

response = client.responses.create(
    model="openai/gpt-4o-mini",
    input="What should I do today?"
)

print(response.output_text)