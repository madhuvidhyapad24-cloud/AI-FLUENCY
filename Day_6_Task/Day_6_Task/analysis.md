# Day 6 — Reliable Tool Calling: Analysis

## 1. Introduction
Reliable tool calling enables an AI application to use external functions safely and consistently. This project uses FarmAssist, an agriculture assistant that estimates irrigation water requirements and suggests water-saving methods.

## 2. Tool-Calling Schemas
A tool schema defines a function's name, description, argument types, required fields, and constraints. Schemas make the expected input explicit, but application-side validation is still necessary.

## 3. Validation
The validator checks:
- Whether the tool exists.
- Whether arguments are a JSON-style object.
- Whether required fields are present.
- Whether values have the correct types.
- Whether numbers fall within permitted ranges.
- Whether unexpected fields or invalid enum values are supplied.

Validation prevents malformed arguments from reaching the tool function.

## 4. Tool-Calling Workflow
1. Receive a tool name and arguments.
2. Check the tool against the allowlist.
3. Validate its arguments.
4. Execute the permitted function.
5. Return the result or a clear error.
6. Retry selected transient execution failures within a fixed limit.

A tool-call request is not proof that the operation succeeded. The application must execute it and check the result.

## 5. Finish Reasons
Common finish-reason categories include:
- `stop`: the response has finished.
- `tool_calls`: the model requests one or more tool executions.
- `length`: generation stopped because a token limit was reached.

Exact labels depend on the provider and API. Applications should handle the finish reasons supported by their chosen model.

## 6. OpenAI-Compatible APIs
An OpenAI-compatible API uses a similar request and response format. Compatibility does not guarantee identical support for every parameter, tool call, streaming event, or strict schema. Provider-specific behavior must be tested.

## 7. Streaming and Non-Streaming
Non-streaming returns the completed response at once. Streaming delivers response chunks as they become available and can improve perceived responsiveness. However, streamed output may be incomplete, so applications must detect completion before parsing a final structured response.

## 8. JSON Mode and Schema-Constrained Output
JSON mode aims to produce syntactically valid JSON. Schema-constrained output aims to follow a specified structure. Support varies by provider and model. Both approaches still need local validation and checks for semantic correctness.

## 9. Fault Injection
Fault injection deliberately introduces invalid inputs or simulated failures to test application behavior. This project tests missing fields, wrong types, out-of-range values, invalid enum values, unexpected fields, unknown tools, and a transient failure.

## 10. Prompt Injection and Safety
Prompt injection occurs when untrusted input attempts to change an application's intended behavior. Tool allowlists, argument validation, authorization, limited permissions, and clear separation of instructions from untrusted data reduce risk. Schema validation alone cannot prevent all prompt injection attacks.

## 11. Retry Strategy
Retries are useful for temporary failures. This project limits execution to two attempts. Invalid arguments are rejected without retrying. Production systems should use backoff for appropriate transient failures and idempotency controls for operations that can cause side effects.

## 12. Structured Output Comparison

| Test | Expected result |
|---|---|
| Plain text | JSON parsing fails |
| Valid JSON | Parsing and schema validation pass |
| Negative area | Schema validation fails |
| Unexpected field | Schema validation fails |

## 13. Experimental Observations
Run the Python scripts and record your actual observations below.

- `validator.py`: Fill in the observed result.
- `agent.py`: Fill in the observed results for successful execution, validation failure, retry, and unknown tool.
- `fault_injection.py`: Fill in the observed results for each injected fault.
- `structured_output.py`: Fill in the observed JSON parsing and schema validation results.

## 14. Limitations
This implementation uses local Python functions and deterministic test data rather than a live language model. It demonstrates reliability patterns but does not measure the real-world performance of an LLM provider. Irrigation estimates are approximate.

## 15. Conclusion
Reliable tool calling requires more than a model generating arguments. Explicit schemas, local validation, an allowlist, bounded retries, fault-injection tests, and structured-output checks help applications handle errors predictably. Production deployments also require authorization, logging, monitoring, and provider-specific testing.