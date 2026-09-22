# AI Fluency – Day 1 Assessment

## Plain Chatbot vs Rule-Based Workflow vs AI Agent

This project demonstrates three approaches to building an AI-powered college course-fee assistant:

- **Plain LLM Chatbot** – Uses an LLM for natural-language responses.
- **Rule-Based Workflow** – Uses predefined Python rules.
- **AI Agent** – Uses an LLM with tools and multi-step execution.

### Course Data

| Course | Fee |
|---|---:|
| CS101 | ₹12,000 |
| AI202 | ₹18,000 |
| DS303 | ₹15,000 |

### AI Agent Tools

- `get_course_fee()` – Retrieves course fees.
- `calculator()` – Performs arithmetic calculations.

### Technologies

Python • Groq • OpenAI SDK • Tool Calling • Git • GitHub

### Project Structure

```text
AI-FLUENCY/
├── Output/
├── agent.py
├── chatbot.py
├── workflow.py
├── tools.py
├── config.py
├── check_setup.py
├── analysis.md
├── requirements.txt
└── .gitignore
