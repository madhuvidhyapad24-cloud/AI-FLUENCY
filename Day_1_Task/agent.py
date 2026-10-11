
import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

client = Groq(api_key=api_key)

# Tool 1: Retrieve course fee
def get_course_fee(course_code):
    fees = {
        "CS101": 12000,
        "AI202": 18000,
        "DS303": 15000
    }
    return {
        "course": course_code,
        "fee": fees.get(course_code.upper(), None)
    }

# Tool 2: Calculate total
def calculate_total(fee1, fee2):
    return {"total": fee1 + fee2}

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Retrieve the fee for a course",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "enum": ["CS101", "AI202", "DS303"]
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_total",
            "description": "Add two course fees",
            "parameters": {
                "type": "object",
                "properties": {
                    "fee1": {"type": "integer"},
                    "fee2": {"type": "integer"}
                },
                "required": ["fee1", "fee2"]
            }
        }
    }
]

print("=" * 50)
print("       GROQ AI AGENT")
print("       Course Fee Assistant")
print("=" * 50)

messages = [
    {
        "role": "system",
        "content": (
            "You are a course fee AI agent. Use the available tools "
            "to retrieve fees and calculate totals. "
            "CS101 costs Rs. 12000, AI202 costs Rs. 18000, "
            "and DS303 costs Rs. 15000. "
            "Find the fees of CS101 and AI202, calculate their total "
            "using the calculation tool, and compare the total with "
            "a budget of Rs. 30000. Explain the result."
        )
    },
    {
        "role": "user",
        "content": "Complete the course fee analysis automatically."
    }
]

functions = {
    "get_course_fee": get_course_fee,
    "calculate_total": calculate_total
}

for step in range(8):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0.1
    )

    message = response.choices[0].message
    messages.append(message)

    if not message.tool_calls:
        print("\nFinal Agent Answer:")
        print(message.content)
        break

    for tool_call in message.tool_calls:
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"\nTool called: {name}")
        print(f"Arguments: {arguments}")

        result = functions[name](**arguments)
        print(f"Tool result: {result}")

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })
else:
    print("Agent stopped after reaching the maximum number of steps.")

print("\nAI agent execution completed.")
