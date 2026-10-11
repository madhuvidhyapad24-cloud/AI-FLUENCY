
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load the existing root .env file
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("MODEL", "openai/gpt-oss-20b")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from the root .env file.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Course information
course_fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

question = "Which course is the cheapest, and how much can I save compared with AI202?"

prompt = f"""
You are a course fee assistant.

Course fees:
{course_fees}

Question: {question}

Give a direct, accurate answer using the provided fees.
Do not use external information.
"""

print("=" * 55)
print("DAY 2 TASK - DIRECT PROMPTING")
print("=" * 55)
print("Question:", question)

response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "Answer questions clearly using the given information."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

answer = response.choices[0].message.content

print("\nModel Answer:")
print(answer)
print("\nApproach: Direct Prompting")
