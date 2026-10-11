
"""Validate tool names and arguments."""

from tools import TOOLS


class ValidationError(ValueError):
    pass


def validate_arguments(tool_name, arguments):
    # Check whether the tool exists
    if tool_name not in TOOLS:
        raise ValidationError("Unknown tool: " + tool_name)

    # Arguments must be a dictionary
    if not isinstance(arguments, dict):
        raise ValidationError("Arguments must be a JSON object")

    schema = TOOLS[tool_name]["parameters"]
    properties = schema["properties"]
    required = schema["required"]

    # Check required fields
    for field in required:
        if field not in arguments:
            raise ValidationError("Missing required field: " + field)

    # Reject unexpected fields
    if schema.get("additionalProperties") is False:
        for field in arguments:
            if field not in properties:
                raise ValidationError("Unexpected field: " + field)

    # Validate each value
    for field, value in arguments.items():
        if field not in properties:
            continue

        rules = properties[field]
        expected_type = rules["type"]

        if expected_type == "number":
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValidationError(field + " must be a number")

            if value < rules.get("minimum", float("-inf")):
                raise ValidationError(field + " is below the minimum")

            if value > rules.get("maximum", float("inf")):
                raise ValidationError(field + " exceeds the maximum")

        elif expected_type == "string":
            if not isinstance(value, str):
                raise ValidationError(field + " must be a string")

            if len(value) < rules.get("minLength", 0):
                raise ValidationError(field + " cannot be empty")

            if "enum" in rules and value not in rules["enum"]:
                raise ValidationError(field + " has an invalid value")

    return True


if __name__ == "__main__":
    test = {
        "area_acres": 2,
        "water_mm_per_day": 5,
        "crop": "tomato"
    }

    try:
        validate_arguments("estimate_water_budget", test)
        print("Validation successful!")
    except ValidationError as error:
        print("Validation failed:", error)
