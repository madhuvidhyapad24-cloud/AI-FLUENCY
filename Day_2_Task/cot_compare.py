
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

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

course_fees = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

question = (
    "A student has a budget of Rs. 16000. "
    "Which courses are affordable, and how much remains "
    "after paying for the cheapest affordable course?"
)

print("=" * 60)
print("DAY 2 TASK - DIRECT PROMPTING VS CoT")
print("=" * 60)
print("Course fees:", course_fees)
print("Question:", question)

# Approach 1: Direct Prompting
direct_prompt = f"""
Course fees: {course_fees}
Question: {question}

Give the answer directly with the final calculation.
"""

direct_response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "Answer accurately using only the given data."
        },
        {"role": "user", "content": direct_prompt}
    ],
    temperature=0
)

direct_answer = direct_response.choices[0].message.content

print("\n--- DIRECT PROMPTING ---")
print(direct_answer)

# Approach 2: Structured reasoning explanation
cot_prompt = f"""
Course fees: {course_fees}
Question: {question}

Solve the problem carefully.
Identify the affordable courses, compare their fees,
show the key arithmetic steps, and state the final answer.
Provide a concise explanation, not private internal reasoning.
"""

cot_response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "You are a careful mathematical assistant."
        },
        {"role": "user", "content": cot_prompt}
    ],
    temperature=0
)

cot_answer = cot_response.choices[0].message.content

print("\n--- STRUCTURED REASONING (CoT-STYLE) ---")
print(cot_answer)

print("\n--- COMPARISON ---")
print("Direct Prompting: requests a concise answer.")
print("CoT-style: requests steps and a concise explanation.")
