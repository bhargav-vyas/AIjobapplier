from dotenv import load_dotenv
import os
from openai import OpenAI
import csv
import datetime


load_dotenv()

print("Loaded Key:", os.getenv("OPENAI_API_KEY"))  # 🟢 Debug line

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
