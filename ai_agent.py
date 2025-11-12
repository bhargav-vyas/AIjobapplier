from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import csv
import datetime


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpret_command(command):
    prompt = f"""
    TASK: Extract job_title and location from this command:
    "{command}"

    Respond only in strict JSON format:
    {{"job_title": "...", "location": "..."}}
    """

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    try:
        return json.loads(text)
    except:
        return {"job_title": "", "location": ""}
