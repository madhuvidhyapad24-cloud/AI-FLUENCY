
"""Test reliability using deliberately injected faults."""

import json
from agent import execute_tool


def run_test(title, tool_name, arguments, fail_once=False):
    print("\n" + "=" * 55)
    print("TEST:", title)

    result = execute_tool(
        tool_name,
        arguments,
        fail_once=fail_once
    )

    print(json.dumps(result, indent=2))


def main():
    print("FARMASSIST - FAULT INJECTION TESTS")

    # Test 1: Valid input
    run_test(
        "Valid input",
        "estimate_water_budget",
        {
            "area_acres": 1,
            "water_mm_per_day": 4,
            "crop": "maize"
        }
    )

    # Test 2: Missing required field
    run_test(
        "Missing required field",
        "estimate_water_budget",
        {
            "area_acres": 1,
            "crop": "maize"
        }
    )

    # Test 3: Wrong data type
    run_test(
        "Wrong data type",
        "estimate_water_budget",
        {
            "area_acres": "one",
            "water_mm_per_day": 4,
            "crop": "maize"
        }
    )

    # Test 4: Value outside allowed range
    run_test(
        "Out-of-range value",
        "estimate_water_budget",
        {
            "area_acres": 1,
            "water_mm_per_day": 500,
            "crop": "maize"
        }
    )

    # Test 5: Invalid enum value
    run_test(
        "Invalid irrigation method",
        "irrigation_tips",
        {
            "crop": "rice",
            "method": "hose"
        }
    )

    # Test 6: Unknown tool
    run_test(
        "Unknown tool",
        "delete_farm",
        {}
    )

    # Test 7: Temporary execution failure
    run_test(
        "Retry after temporary failure",
        "irrigation_tips",
        {
            "crop": "tomato",
            "method": "drip"
        },
        fail_once=True
    )


if __name__ == "__main__":
    main()
