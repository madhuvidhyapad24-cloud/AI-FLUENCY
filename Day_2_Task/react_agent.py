
import os
import json
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

COURSE_FEES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000
}

# Tool 1: Look up a course fee
def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code in COURSE_FEES:
        return {
            "course": course_code,
            "fee": COURSE_FEES[course_code]
        }

    return {"error": "Course not found"}


# Tool 2: Calculate the remaining budget
def calculate_remaining(budget, fee):
    return {
        "budget": budget,
        "fee": fee,
        "remaining": budget - fee
    }


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its code.",
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
            "name": "calculate_remaining",
            "description": "Calculate budget minus course fee.",
            "parameters": {
                "type": "object",
                "properties": {
                    "budget": {"type": "integer"},
                    "fee": {"type": "integer"}
                },
                "required": ["budget", "fee"]
            }
        }
    }
]

tool_functions = {
    "get_course_fee": get_course_fee,
    "calculate_remaining": calculate_remaining
}

messages = [
    {
        "role": "system",
        "content": (
            "You are a course-fee assistant. Use the available tools "
            "to look up course fees and calculate amounts. "
            "Explain the result briefly. Never invent a fee."
        )
    },
    {
        "role": "user",
        "content": (
            "My budget is Rs. 16000. Find the cheapest course I can "
            "afford from CS101, AI202, and DS303. Use the tools "
            "to check fees and calculate the remaining budget."
        )
    }
]

print("=" * 60)
print("DAY 2 TASK - ReAct AGENT")
print("=" * 60)

for step in range(8):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message
    messages.append(message.model_dump(exclude_none=True))

    if not message.tool_calls:
        print("\nFinal Answer:")
        print(message.content)
        break

    for tool_call in message.tool_calls:
        name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        print(f"\nAction: {name}")
        print("Input:", arguments)

        if name not in tool_functions:
            result = {"error": "Unknown tool"}
        else:
            result = tool_functions[name](**arguments)

        print("Observation:", result)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })
else:
    print("Stopped: maximum tool-call rounds reached.")
