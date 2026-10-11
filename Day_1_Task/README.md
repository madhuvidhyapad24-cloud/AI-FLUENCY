# Day 1 Task – Comparing Chatbots, Workflows, and AI Agents

## Overview

This project compares three approaches to solving the same problem: a **Plain Chatbot, a Rule-Based Workflow, and an AI Agent**. A course fee assistant is used as the common scenario to evaluate flexibility, decision-making, tool usage, and automation.

## Objective

- Build a plain chatbot using a Large Language Model (LLM).
- Implement a rule-based workflow using Python.
- Build an AI agent that uses an LLM and tools.
- Compare the strengths, limitations, and suitable use cases of all three approaches.

## Scenario: Course Fee Assistant

The application works with the following course fee information:

| Course Code | Course Fee |
|---|---:|
| CS101 | ₹12,000 |
| AI202 | ₹18,000 |
| DS303 | ₹15,000 |

## Technologies Used

- **Python** – Application development
- **Groq API** – LLM-powered responses and agent reasoning
- **Function Calling** – Connecting the AI agent to executable tools
- **python-dotenv** – Loading environment variables
- **Git and GitHub** – Version control and project hosting

## Project Structure

```text
Day_1_Task/
├── chatbot.py
├── workflow.py
├── agent.py
├── analysis.md
├── README.md
└── Output/
    ├── chatbot_output.png
    ├── workflow_output.png
    └── agent_output.png
```

The screenshot filenames above are examples. Use your actual filenames in the `Output` folder.

## Implementations

### 1. Plain Chatbot – `chatbot.py`

Uses the Groq LLM to answer predefined course fee questions in natural language.

**Key feature:** Flexible, human-readable responses.

### 2. Rule-Based Workflow – `workflow.py`

Uses predefined Python instructions, conditions, and arithmetic operations to display fees and evaluate budgets.

**Key feature:** Predictable and repeatable execution without an LLM API call.

### 3. AI Agent – `agent.py`

Uses an LLM, function tools, and an execution loop to retrieve course fees and calculate totals.

**Key feature:** Tool-assisted, multi-step problem solving.

## How to Run

Run the commands from the project root directory:

```bash
python Day_1_Task/chatbot.py
python Day_1_Task/workflow.py
python Day_1_Task/agent.py
```

The chatbot and agent require a valid Groq API key and the required Python packages. The rule-based workflow runs independently.

## Environment Setup

Install the required packages:

```bash
python -m pip install groq python-dotenv
```

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Replace the placeholder with your actual API key. Never commit `.env` to GitHub.

## Comparison Summary

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| LLM | Yes | No | Yes |
| Execution | Generates responses | Follows fixed rules | Selects and calls tools |
| Flexibility | Conversational | Limited to programmed rules | Supports multi-step tasks |
| Predictability | Model-dependent | High | Depends on model and tools |
| Best suited for | Conversational assistance | Repetitive, fixed tasks | Tool-assisted automation |

## Results and Analysis

The three implementations demonstrate different approaches to the same course fee scenario. The chatbot focuses on natural-language answers, the workflow focuses on deterministic execution, and the agent combines model reasoning with tool execution.

Detailed observations and conclusions are documented in [`analysis.md`](analysis.md). Execution evidence is available in the `Output/` folder.

## Security

- Keep API keys in `.env`.
- Exclude `.env` and `.venv` from version control.
- Validate tool inputs and outputs before relying on them.

## Conclusion

This assessment demonstrates how plain chatbots, rule-based workflows, and AI agents differ in flexibility, predictability, and automation. Choosing the right approach depends on the task, the need for tool usage, and the level of reliability required.