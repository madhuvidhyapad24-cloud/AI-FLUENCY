# Day 1 Assessment – Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The chosen scenario is a private college course-fee assistant.

The system contains private course-fee information:

| Course | Fee |
|---|---:|
| CS101 | ₹12,000 |
| AI202 | ₹18,000 |
| DS303 | ₹15,000 |

The system is tested using course-fee questions, calculations, a welcome-message question, and a budget-based challenge.

## 2. Explanation of Each Approach

### 2.1 Plain Chatbot

The plain chatbot uses an LLM to answer user questions. It does not have access to the private course-fee data and does not use any tools.

For the course-fee questions, the chatbot could not provide the private fees. However, it handled the general welcome-message question well.

How it works:

**User question → LLM → Answer**

Limitation: It cannot reliably answer questions that require private college data.

### 2.2 Rule-Based Workflow

The rule-based workflow uses predefined Python if/else rules. It does not use an LLM or external tools.

It correctly handled predefined fee questions, including the AI202 fee and the total fee after a scholarship. It did not handle questions outside its predefined rules.

How it works:

**User question → Python rules → Answer**

Limitation: It has low flexibility and depends on predefined conditions.

### 2.3 AI Agent

The AI agent combines an LLM, tools, and a loop.

The agent uses `get_course_fee()` to retrieve private course fees and `calculator()` to perform arithmetic. The LLM decides which tool is required, Python executes the tool, and the result is returned to the LLM.

For the scholarship question, the agent retrieved both course fees and then used the calculator to obtain the final amount of ₹27,000.

How it works:

**User question → LLM → Tool → Result → LLM → Final answer**

Limitation: It is more complex and may require multiple LLM calls and tool executions.

## 3. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| Flexibility | High | Low | High |
| Decision-making | LLM generates response | Fixed rules | LLM selects actions/tools |
| Tool usage | No | No | Yes |
| Private-data access | No | Yes | Yes, through tools |
| Multi-step task handling | Limited | Predefined only | Yes |
| Automation | Response generation | High for fixed tasks | High |
| Reliability | May not know private data | High for predefined cases | Good when tools are correctly designed |

## 4. Suitability Analysis

For the private college course-fee assistant, the AI agent is suitable because it can understand natural-language questions, access private data through tools, perform calculations, and handle multi-step tasks.

A rule-based workflow is suitable when the questions and conditions are predictable and predefined.

A plain chatbot is suitable for general conversation and questions that do not require private data.

## 5. Conclusion

A plain chatbot is suitable for general conversation and natural-language responses.

A rule-based workflow is suitable for predictable tasks with fixed rules.

An AI agent is suitable for tasks requiring natural-language understanding, private-data access, tool usage, decision-making, and multiple steps.

**Chatbot = LLM + conversation**

**Workflow = fixed rules + predictable execution**

**Agent = LLM + tools + loop**