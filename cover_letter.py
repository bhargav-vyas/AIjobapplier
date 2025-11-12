from dotenv import load_dotenv
from openai import OpenAI
import os
import csv
import datetime


# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_cover_letter(job_title, company_name, skills):
    prompt = f"""
    Write a concise, professional, and friendly cover letter for a {job_title} position at {company_name}.
    Highlight the following skills: {', '.join(skills)}.
    Keep it short — 4 to 5 sentences maximum.
    """

    response = client.chat.completions.create(
        model="gpt-5",  # ✅ use your GPT-5 access here
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
