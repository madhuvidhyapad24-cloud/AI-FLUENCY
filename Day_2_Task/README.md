# Day 2 Task: Reasoning and Acting in AI

## 📌 Project Overview

This project compares four AI approaches: Direct Prompting, Chain-of-Thought-style Prompting, ReAct Agents, and Self-Consistency. A course-fee assistant scenario is used to evaluate how these approaches answer questions, explain calculations, use tools, and produce consistent results.

## 🎯 Objectives

- Understand different AI prompting and reasoning approaches.
- Compare direct answers with structured explanations.
- Implement a ReAct agent that uses tools.
- Evaluate repeated model responses using self-consistency.
- Analyze the strengths, limitations, and suitability of each approach.

## 🛠️ Technologies Used

- **Language:** Python
- **LLM Provider:** Groq
- **Model:** `openai/gpt-oss-20b`
- **Libraries:** OpenAI Python SDK, python-dotenv
- **Tools:** VS Code, Git, GitHub

## 📂 Project Structure

```text
Day_2_Task/
├── direct_prompting.py
├── cot_compare.py
├── react_agent.py
├── self_consistency.py
├── analysis.md
├── README.md
└── screenshots/
    ├── direct_prompting.png
    ├── cot_compare.png
    ├── react_agent.png
    └── self_consistency.png
```

## 🧪 Experiments

### 1. Direct Prompting
Sends a question directly to the language model and evaluates its answer.

### 2. Chain-of-Thought-Style Prompting
Requests a structured explanation with key calculation steps to make the answer easier to verify.

### 3. ReAct Agent
Combines model responses with tool execution. The agent uses course-fee lookup and budget-calculation tools to solve the problem.

### 4. Self-Consistency
Repeats the same question multiple times at a non-zero temperature and compares the generated responses.

## 💰 Scenario: Course Fee Assistant

| Course Code | Fee |
|---|---:|
| CS101 | ₹12,000 |
| AI202 | ₹18,000 |
| DS303 | ₹15,000 |

**Budget:** ₹16,000

**Expected result:** CS101 is the cheapest affordable course, and the remaining budget is ₹4,000.

## ▶️ How to Run

Run these commands from the main project directory:

```powershell
python .\Day_2_Task\direct_prompting.py
python .\Day_2_Task\cot_compare.py
python .\Day_2_Task\react_agent.py
python .\Day_2_Task\self_consistency.py
```

## 📊 Results and Analysis

The experiments compare answer accuracy, explanation quality, tool usage, implementation complexity, and consistency.

Refer to [`analysis.md`](analysis.md) for the detailed comparison, observations, suitability analysis, and conclusion. Actual experimental observations should be recorded after running the programs.

## 📸 Screenshots

The `screenshots/` directory contains the actual execution outputs for each experiment.

## 🔐 Configuration

Store the Groq API key in the root `.env` file. Do not commit `.env`, API keys, or other secrets to GitHub.

Required environment variable:

```text
GROQ_API_KEY=your_groq_api_key
```

Install the required libraries if they are not already available in your virtual environment:

```powershell
pip install openai python-dotenv
```

## ✅ Conclusion

This project demonstrates how different prompting and agent approaches can solve the same problem in different ways. Direct prompting is suitable for simple questions, structured prompting helps communicate key calculation steps, ReAct supports tool-based tasks, and self-consistency helps compare repeated outputs.

The most suitable approach depends on task complexity, tool requirements, and the need to validate results.

---

**Project:** Day 2 – AI Fluency Assessment  
**Repository:** [AI-FLUENCY](https://github.com/madhuvidhyapad24-cloud/AI-FLUENCY)
