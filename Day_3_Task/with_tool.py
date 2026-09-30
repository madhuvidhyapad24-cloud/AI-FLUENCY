import sys
import json

sys.path.append("../Day_1")

from config import client, MODEL
from calculator_tool import calculate_fee


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_fee",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Mathematical expression to calculate"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


question = """
Calculate the total fee for CS101 and AI202 after a 10% scholarship.

CS101 = 12000
AI202 = 18000
Scholarship = 10%

Use the calculator tool to calculate the final amount.
"""

messages = [
    {"role": "user", "content": question}
]


response = client.chat.completions.create(
    model=MODEL,
    messages=messages,
    tools=tools,
    tool_choice="required",
    temperature=0
)

message = response.choices[0].message


if message.tool_calls:

    call = message.tool_calls[0]

    args = json.loads(call.function.arguments)

    result = calculate_fee(args["expression"])

    print("Tool called:", call.function.name)
    print("Expression:", args["expression"])
    print("Tool result:", result)

    messages.append({
        "role": "assistant",
        "content": message.content or "",
        "tool_calls": [
            {
                "id": call.id,
                "type": "function",
                "function": {
                    "name": call.function.name,
                    "arguments": call.function.arguments
                }
            }
        ]
    })

    messages.append({
        "role": "tool",
        "tool_call_id": call.id,
        "content": str(result)
    })

    final_response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0
    )

    print("Final answer:")
    print(final_response.choices[0].message.content)

else:
    print("No tool call was made.")