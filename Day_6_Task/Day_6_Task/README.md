# Day 6 — Reliable Tool Calling

## Project Title
**FarmAssist: Reliable Tool Calling with Validation, Retries, and Structured Outputs**

## 1. Objective
To demonstrate reliable tool calling through input validation, controlled retries, fault injection, and structured JSON output verification.

## 2. Scenario
FarmAssist is a smart agriculture assistant that estimates irrigation water requirements and provides practical water-saving tips.

## 3. Technologies Used
- Python
- JSON
- JSON Schema concepts
- Exception handling
- Input validation
- Fault injection and retry logic

## 4. Project Files

| File | Purpose |
|---|---|
| `tools.py` | Defines tools and their functions |
| `validator.py` | Validates tool arguments |
| `agent.py` | Executes tools and handles retries |
| `fault_injection.py` | Tests invalid inputs and failures |
| `structured_output.py` | Compares JSON parsing and schema validation |
| `analysis.md` | Concepts, observations, and conclusion |

## 5. How to Run

Open the terminal in this folder and execute:

```bash
python validator.py
python agent.py
python fault_injection.py
python structured_output.py
```

## 6. Key Features
- Allowlisted tool execution
- Required-field validation
- Type and range checks
- Rejection of unexpected fields
- Retry after a simulated temporary failure
- JSON parsing and schema validation
- Fault-injection experiments

## 7. Expected Results
Valid inputs should execute successfully. Invalid arguments and unknown tools should be rejected. A simulated temporary failure should recover on the second attempt. Invalid JSON or schema data should be detected.

## 8. Limitations
This project is a local demonstration and does not call a live language model. The water budget is an approximate calculation and should not replace professional agricultural advice.

## 9. Conclusion
The project demonstrates how validation, allowlisted tools, bounded retries, and structured output checks can improve the reliability of AI tool-calling applications.