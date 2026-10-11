
# Day 1 Task: Comparing Chatbots, Workflows, and AI Agents

## 1. Objective

The objective is to compare a plain LLM chatbot, a rule-based workflow, and an AI agent using the same course fee assistant scenario.

## 2. Scenario

The system provides course fee information and calculates the total cost of courses.

| Course | Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

## 3. Plain Chatbot

The plain chatbot uses the Groq LLM to answer predefined questions. It generates natural-language responses using the supplied course fee information.

**Advantages**
- Natural and flexible responses.
- Understands questions written in ordinary language.
- Easy to build for simple conversations.

**Limitations**
- Does not independently execute calculation tools.
- Responses depend on the model and the information provided.

## 4. Rule-Based Workflow

The workflow uses predefined Python instructions, conditions, and arithmetic operations.

**Advantages**
- Predictable and repeatable results.
- Accurate calculations for the defined rules.
- Does not require an LLM API call.

**Limitations**
- Handles only the situations programmed in advance.
- Cannot independently adapt to unfamiliar requests.

## 5. AI Agent

The AI agent uses the Groq LLM, function tools, and a loop. It can request course fee information from a tool, calculate totals using another tool, and use the returned results to formulate a final answer.

**Advantages**
- Can select tools according to the task.
- Supports multi-step problem solving.
- Combines language understanding with program execution.

**Limitations**
- Requires additional implementation and testing.
- Depends on model availability and API connectivity.
- Tool calls must be validated to prevent incorrect operations.

## 6. Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| LLM used | Yes | No | Yes |
| Fixed rules | Prompt and instructions | Yes | Tool logic and instructions |
| Tool execution | No | Direct Python operations | LLM-directed tool calls |
| Flexibility | High for conversation | Low | High |
| Multi-step tasks | Limited | Predefined steps | Can select tools across steps |
| Predictability | Model-dependent | High | Model- and tool-dependent |
| API dependency | Yes | No | Yes |

## 7. Suitability

- **Plain chatbot:** Best for answering questions and conversational assistance.
- **Rule-based workflow:** Best for predictable tasks with fixed rules.
- **AI agent:** Best for tasks requiring decisions, multiple steps, and tool usage.

## 8. Conclusion

The three approaches solve the same course fee problem in different ways. The plain chatbot focuses on natural-language responses, the rule-based workflow follows fixed instructions, and the AI agent combines an LLM with executable tools. The most suitable approach depends on the task's complexity, reliability requirements, and need for automation.

## 9. Evidence

Screenshots of the chatbot, workflow, and agent execution are stored in the `Output` folder. These demonstrate the implementations and their observed outputs.
