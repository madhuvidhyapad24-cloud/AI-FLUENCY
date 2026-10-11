import sys
sys.path.append("../Day_1")

from config import client, MODEL

question = """
What is the total fee for CS101 and AI202 after a 10% scholarship?
CS101 fee is Rs. 12000 and AI202 fee is Rs. 18000.
"""

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": question}
    ]
)

print("Question:", question)
print("Answer:", response.choices[0].message.content)