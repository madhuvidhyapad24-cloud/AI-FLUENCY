# Day 2 Task – Direct Prompting vs Chain-of-Thought vs ReAct Agent

## 3.1 Explanation of Each Approach

### Direct Prompting

Direct prompting asks the model to give an answer directly using its existing knowledge.

- It can answer simple questions and general knowledge questions.
- It does not use external tools.
- It gives the answer immediately without showing detailed reasoning.
- It may be less reliable for multi-step calculations or questions requiring external data.
- In this scenario, it can calculate the course costs, but it does not independently verify the fee information using a tool.

### Chain-of-Thought (CoT)

Chain-of-Thought prompting asks the model to solve the problem step by step.

- It is useful for multi-step calculations and logical questions.
- It does not use external tools in this experiment.
- The model shows the calculation steps before giving the final answer.
- It can improve reasoning on problems where all required information is already provided.
- However, it cannot obtain unknown or external information by itself.

### ReAct Agent

ReAct combines reasoning with actions and observations.

- It can reason about what information is required.
- It uses tools when external information or calculations are needed.
- It observes the tool results and continues reasoning.
- It is useful for multi-step problems involving external data.
- In this scenario, the agent used `get_course_fee` to obtain course fees and `calculator` to perform the calculations.
- It continues until it has enough information to produce the final answer.

---

## 3.2 Comparison Table

| Basis for comparison | Direct Prompting | Chain-of-Thought | ReAct Agent |
|---|---|---|---|
| Reasoning depth | Low | High | High |
| Tool usage | No tools | No tools | Uses tools when required |
| Reliability on multi-step questions | Moderate | Higher for given information | High when correct tools are available |
| Transparency | Final answer only | Shows calculation steps | Shows actions and observations |
| Speed / cost | Fast and low cost | Slower and more tokens | More tool calls, so higher cost |
| Consistency across repeated runs | Usually consistent at low temperature | Can vary with higher temperature | Depends on model and tool execution |

---

## 3.3 Self-Consistency Observation

The first question was used for self-consistency testing.

The model was run 5 times with temperature = 0.8.

### Answers observed

- Run 1: Rs. 9,562.5 per instalment
- Run 2: Rs. 9,562.5 per instalment
- Run 3: Rs. 9,562.5 per instalment
- Run 4: Rs. 9,562.5 per instalment
- Run 5: Rs. 9,562.5 per instalment

The answers had slightly different wording, but they gave the same numerical answer.

### Majority Answer

**Rs. 9,562.5 per instalment**

The majority answer was correct.

When temperature is changed to 0, repeated runs are expected to become nearly identical because the model becomes more deterministic. Therefore, self-consistency voting provides little additional benefit at temperature 0.

---

## 3.4 Suitability Analysis

For this course-fee scenario, the **ReAct agent** is suitable because the problem requires course-fee information and calculations.

Direct prompting can provide an immediate answer, but it does not use tools to verify the course fees.

Chain-of-Thought can improve step-by-step calculation when all required information is already available in the question. However, it cannot obtain information from external tools.

The ReAct agent can obtain the course fees using `get_course_fee`, perform calculations using the `calculator` tool, observe the results, and then provide the final answer.

Therefore, for this particular scenario involving tool-based information and multi-step calculations, ReAct provides the required tool usage and reasoning process.

---

## 3.5 Conclusion

Direct prompting, Chain-of-Thought, and ReAct solve problems in different ways.

Direct prompting is suitable for simple questions where the model already has the required information.

Chain-of-Thought is useful for multi-step reasoning when all the required information is available in the question.

ReAct is useful when a problem requires both reasoning and interaction with external tools.

This experiment showed that Chain-of-Thought produced step-by-step calculations, while the ReAct agent used tools to obtain course fees and perform calculations. Self-consistency also showed that repeated reasoning runs can produce the same final answer even when the wording differs.

For problems requiring external information and tool-based calculations, the ReAct approach is appropriate because it combines reasoning, actions, observations, and a final answer.