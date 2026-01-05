from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

text = "I like to play cricket and my asian friend likes to eat crickets but that is different."

response = client.embeddings.create(
    model="openai/text-embedding-3-small",
    input=text
)

print(len(response.data[0].embedding))
print(response.data[0].embedding[:8])