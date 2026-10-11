
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

questions = [
    "What is the fee for CS101?",
    "Which course has the highest fee?",
    "What is the total fee for CS101 and AI202?"
]

print("=" * 45)
print("       GROQ PLAIN CHATBOT")
print("       Course Fee Assistant")
print("=" * 45)

for question in questions:
    print(f"\nUser: {question}")

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a course fee assistant. "
                    "CS101 costs Rs. 12000, AI202 costs Rs. 18000, "
                    "and DS303 costs Rs. 15000. "
                    "Answer using these fees only."
                )
            },
            {"role": "user", "content": question}
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content
    print(f"Chatbot: {answer}")

print("\n" + "=" * 45)
print("       CHATBOT COMPLETED")
print("=" * 45)
