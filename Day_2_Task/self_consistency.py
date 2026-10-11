
import os
from pathlib import Path
from collections import Counter
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

question = """
Course fees:
CS101 = Rs. 12000
AI202 = Rs. 18000
DS303 = Rs. 15000

A student has a budget of Rs. 16000.
Which is the cheapest affordable course?
Return the course code and fee in this format:
COURSE=CS101;FEE=12000
"""

answers = []

print("=" * 60)
print("DAY 2 TASK - SELF-CONSISTENCY EXPERIMENT")
print("=" * 60)

# Repeat the same question five times
for i in range(5):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer using only the given course fees. "
                    "Return the requested format accurately."
                )
            },
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )

    answer = response.choices[0].message.content.strip()
    answers.append(answer)

    print(f"\nAttempt {i + 1}:")
    print(answer)

# Count identical full responses
counts = Counter(answers)
most_common_answer, count = counts.most_common(1)[0]

print("\n" + "=" * 60)
print("EXPERIMENT SUMMARY")
print("=" * 60)
print("Total attempts:", len(answers))
print("Most repeated exact response:", most_common_answer)
print("Exact-response count:", count, "out of", len(answers))
print("Exact-response agreement:", f"{count / len(answers) * 100:.1f}%")

print("\nExpected correct answer: CS101, Rs. 12000")
print("Check the five actual answers to evaluate correctness.")
print("Note: Identical wording is not required for a correct answer.")
