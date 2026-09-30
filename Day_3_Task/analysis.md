# From Prompt to Action – Understanding LLMs, Tools and Agents

## Scenario

My scenario is a College Course Fee Assistant.

CS101 = Rs. 12,000  
AI202 = Rs. 18,000  
Scholarship = 10%

Total before scholarship:

12000 + 18000 = Rs. 30,000

Final fee:

30000 × 0.90 = Rs. 27,000

## 1. What is an LLM?

A Large Language Model (LLM) is an AI model that understands and generates human language.

In this scenario, the LLM understands the student's fee question and provides an answer.

## 2. What is an Agent?

An agent is an LLM that can decide when to use a tool, call the tool, receive the result, and provide a final answer.

In this scenario, the agent uses the calculator tool to calculate the final fee.

## 3. What is a Tool and Tool Call?

A tool is an external function that gives the LLM an additional capability.

My tool is:

calculate_fee(expression)

A tool call is a request from the LLM to use that tool with specific input.

Example:

calculate_fee("30000 * 0.9")

Tool result:

27000.0

## 4. Tool Call Flow

1. User asks for the total course fee.
2. LLM receives the question.
3. LLM decides that calculation is required.
4. LLM calls the calculator tool.
5. Calculator performs the calculation.
6. Tool returns 27000.0.
7. Result is sent back to the LLM.
8. LLM gives the final answer of Rs. 27,000.

## 5. Plain LLM vs LLM with One Tool

| Plain LLM | LLM with Calculator Tool |
|---|---|
| Answers directly | Uses an external calculator |
| No tool call | Makes a tool call |
| Calculation is done by the model | Calculation is performed by the calculator |
| Less transparent | Tool result can be verified |

## 6. Observations

The plain LLM answered the question directly and calculated the fee.

The tool-enabled LLM called the calculate_fee tool.

The calculator returned 27000.0.

The final answer was Rs. 27,000.

The tool makes the numerical calculation explicit and easier to verify.

## 7. Conclusion

An LLM can understand questions and generate answers. Tools give an LLM additional capabilities such as calculation.

An agent combines the LLM with tools and decides when to use them.

This experiment demonstrates the difference between a plain LLM and an LLM that can use an external calculator tool.