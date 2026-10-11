
"""Compare plain text, JSON, and schema-validated outputs."""

import json
from tools import TOOLS
from validator import validate_arguments, ValidationError


def check_output(title, response):
    print("\n" + "=" * 55)
    print("MODE:", title)
    print("RAW OUTPUT:", response)

    # First check whether the response is valid JSON
    try:
        data = json.loads(response)
        print("JSON parsing: PASS")

    except json.JSONDecodeError as error:
        print("JSON parsing: FAIL")
        print("Reason:", error)
        print("Schema validation: NOT RUN")
        return

    # Then validate the parsed JSON against the tool schema
    try:
        validate_arguments("estimate_water_budget", data)
        print("Schema validation: PASS")

    except ValidationError as error:
        print("Schema validation: FAIL")
        print("Reason:", error)


def main():
    print("FARMASSIST - STRUCTURED OUTPUT COMPARISON")

    # Example 1: Plain text is not JSON
    check_output(
        "Plain text",
        "The farmer should use drip irrigation to save water."
    )

    # Example 2: Valid JSON with correct fields
    check_output(
        "Valid JSON",
        '{"area_acres": 2, "water_mm_per_day": 5, "crop": "tomato"}'
    )

    # Example 3: JSON with invalid values
    check_output(
        "Invalid schema data",
        '{"area_acres": -2, "water_mm_per_day": 5, "crop": "tomato"}'
    )

    # Example 4: JSON with an unexpected field
    check_output(
        "Unexpected field",
        '{"area_acres": 2, "water_mm_per_day": 5, "crop": "tomato", "extra": true}'
    )


if __name__ == "__main__":
    main()
