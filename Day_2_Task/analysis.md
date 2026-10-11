
# Day 2 Task: Reasoning and Acting in AI

## 1. Objective

The objective of this experiment is to compare Direct Prompting,
Chain-of-Thought-style prompting, ReAct agents, and Self-Consistency
using a course-fee assistant scenario.

## 2. Scenario

A student wants to choose an affordable course within a budget of
Rs. 16,000.

| Course Code | Course Fee |
|---|---:|
| CS101 | Rs. 12,000 |
| AI202 | Rs. 18,000 |
| DS303 | Rs. 15,000 |

The cheapest affordable course is CS101, costing Rs. 12,000.
The remaining budget is Rs. 4,000.

## 3. Approach 1: Direct Prompting

Direct prompting provides the question and course-fee information
to the language model and requests an answer directly.

**Observation:** The model is expected to identify CS101 as the
cheapest affordable course and calculate the remaining budget.

**Advantages:**
- Simple to implement.
- Fast for straightforward questions.
- Requires fewer instructions.

**Limitations:**
- Complex tasks may need more structured instructions.
- The answer must be checked for accuracy.

## 4. Approach 2: Chain-of-Thought-Style Prompting

This approach asks the model to provide a concise explanation,
identify affordable courses, and show the key arithmetic steps.

**Observation:** The response can be compared with direct prompting
to see whether a structured explanation improves clarity.

**Advantages:**
- Makes calculations easier to inspect.
- Helps identify mistakes in intermediate steps.
- Useful for multi-step questions.

**Limitations:**
- May produce longer responses.
- An explanation does not guarantee correctness.

## 5. Approach 3: ReAct Agent

ReAct combines model decisions with actions performed through tools.
This experiment uses two tools:

1. `get_course_fee()` retrieves a course fee.
2. `calculate_remaining()` calculates the remaining budget.

**Observation:** The program prints the tool actions, their inputs,
and the returned observations before displaying the final answer.

**Advantages:**
- Uses tools to retrieve information and perform calculations.
- Suitable for multi-step tasks.
- Makes tool usage observable.

**Limitations:**
- Requires additional implementation.
- Tool calls can fail or use incorrect arguments.
- The final answer still requires validation.

## 6. Approach 4: Self-Consistency

The same question is sent to the model five times using a
non-zero temperature.

The responses are recorded and compared.

**Observation:** Fill in the following details from the actual
execution of `self_consistency.py`.

- Total attempts: 5
- Number of correct answers: [Fill in actual result]
- Most common answer: [Fill in actual result]
- Exact-response agreement: [Fill in actual result]

Self-consistency can help assess agreement across multiple outputs.
However, agreement alone does not prove that an answer is correct.

## 7. Comparison Table

| Criterion | Direct Prompting | CoT-Style | ReAct | Self-Consistency |
|---|---|---|---|---|
| Main purpose | Direct answer | Explain key steps | Use tools and observations | Compare repeated answers |
| Tool usage | No | No | Yes | No |
| Output | Concise answer | Structured explanation | Actions and final answer | Multiple answers |
| Complexity | Low | Low to medium | High | Medium |
| Main limitation | May miss details | Explanation may be wrong | Tool failures | Repeated answers may agree incorrectly |

## 8. Suitability Analysis

Direct prompting is suitable for simple questions such as checking
a course fee.

CoT-style prompting is useful when the user needs a concise
explanation of a calculation.

ReAct is suitable when a task requires retrieving information and
performing calculations through tools. It is the most appropriate
of these approaches when tool use is essential to the task.

Self-consistency is useful when we want to compare multiple
generated answers, but the outputs must still be checked against
the known correct answer.

## 9. Conclusion

This experiment demonstrates four different ways of solving a
course-fee problem with a language model.

Direct prompting is simple, CoT-style prompting encourages
structured explanations, ReAct enables tool-based actions, and
self-consistency compares repeated responses.

The appropriate approach depends on task complexity, the need
for external tools, and the importance of checking correctness.

## 10. Evidence

Add screenshots of the actual outputs from all four Python
programs in the `screenshots` folder.

The screenshots should show the program name, relevant output,
and final result.
