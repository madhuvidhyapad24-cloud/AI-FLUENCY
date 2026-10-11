
"""FarmAssist: reliable tool-calling workflow."""

import json

from tools import TOOLS, estimate_water_budget, irrigation_tips
from validator import validate_arguments, ValidationError


# Allow only these registered tools
FUNCTIONS = {
    "estimate_water_budget": estimate_water_budget,
    "irrigation_tips": irrigation_tips
}


def execute_tool(tool_name, arguments, fail_once=False):
    """Validate inputs and retry a temporary execution failure."""
    max_attempts = 2

    for attempt in range(1, max_attempts + 1):
        try:
            # Validate before executing the tool
            validate_arguments(tool_name, arguments)

            if fail_once and attempt == 1:
                raise RuntimeError("Temporary simulated failure")

            result = FUNCTIONS[tool_name](**arguments)

            return {
                "success": True,
                "tool": tool_name,
                "attempts": attempt,
                "result": result
            }

        except ValidationError as error:
            return {
                "success": False,
                "tool": tool_name,
                "attempts": attempt,
                "error_type": "validation",
                "error": str(error)
            }

        except Exception as error:
            if attempt == max_attempts:
                return {
                    "success": False,
                    "tool": tool_name,
                    "attempts": attempt,
                    "error_type": "execution",
                    "error": str(error)
                }

    return {"success": False, "error": "Unexpected failure"}


def main():
    print("=" * 55)
    print("FARMASSIST - RELIABLE TOOL CALLING")
    print("=" * 55)

    # Test 1: Valid tool call
    result = execute_tool(
        "estimate_water_budget",
        {
            "area_acres": 2,
            "water_mm_per_day": 5,
            "crop": "tomato"
        }
    )
    print("\nTEST 1: Valid water budget")
    print(json.dumps(result, indent=2))

    # Test 2: Invalid arguments
    result = execute_tool(
        "estimate_water_budget",
        {"area_acres": 2, "crop": "tomato"}
    )
    print("\nTEST 2: Missing required field")
    print(json.dumps(result, indent=2))

    # Test 3: Retry after a temporary failure
    result = execute_tool(
        "irrigation_tips",
        {"crop": "tomato", "method": "drip"},
        fail_once=True
    )
    print("\nTEST 3: Retry after temporary failure")
    print(json.dumps(result, indent=2))

    # Test 4: Unknown tool
    result = execute_tool("unknown_tool", {})
    print("\nTEST 4: Unknown tool")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
