"""Tools used by the AI agent."""

import ast
import operator
from config import COURSE_FEES


def get_course_fee(course_code):
    """Return the fee for a course code."""
    fee = COURSE_FEES.get(course_code)

    if fee is None:
        return "Course not found"

    return str(fee)


def calculator(expression):
    """Safely calculate a basic arithmetic expression."""

    operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }

    def calculate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.UnaryOp) and type(node.op) in operators:
            return operators[type(node.op)](calculate(node.operand))

        if isinstance(node, ast.BinOp) and type(node.op) in operators:
            return operators[type(node.op)](
                calculate(node.left),
                calculate(node.right)
            )

        raise ValueError("Invalid expression")

    try:
        tree = ast.parse(expression, mode="eval")
        return str(calculate(tree.body))
    except Exception:
        return "Invalid calculation"


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee for a course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "Course code such as CS101, AI202 or DS303."
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate a basic arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression such as (12000+18000)*0.9."
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


TOOL_FUNCTIONS = {
    "get_course_fee": get_course_fee,
    "calculator": calculator
}