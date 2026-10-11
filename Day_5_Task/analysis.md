
# Day 5 Task: Serving Models Your Way

## 1. Scenario

The scenario is FarmAssist, a local smart-agriculture assistant.
It answers general farming questions using a customized Ollama model.

The computer has 15.82 GB of physical RAM. The base model is
Qwen2.5 3B, and the custom model is named `farm-assist`.

The application uses an Ollama Modelfile to define a system prompt,
temperature and context-length setting.

## 2. Explanation of Concepts

### 2.1 What is Ollama?

Ollama is a tool for downloading, managing and running language
models locally. It provides a command-line interface and a local
HTTP API.

Model files are managed by Ollama rather than being manually
loaded by the Python application. The Python program sends requests
to the Ollama service, which returns generated responses.

### 2.2 What is a Modelfile?

A Modelfile describes how to create a customized Ollama model.

This project uses:

- FROM: selects the base model.
- PARAMETER temperature: controls response variability.
- PARAMETER num_ctx: configures the context window.
- SYSTEM: provides instructions that guide the assistant.

These settings customize model behavior without retraining
the base model.

### 2.3 What happens when a request arrives?

The Python application sends a prompt to the Ollama API.
Ollama loads or accesses the model, processes the prompt and
generates a response.

The client can request a complete response or receive output
incrementally through streaming.

### 2.4 OpenAI-compatible APIs

An OpenAI-compatible endpoint accepts requests using an API format
similar to the OpenAI API. Compatibility does not guarantee that
every parameter or feature is supported identically.

Ollama provides an OpenAI-compatible API for supported endpoints.
vLLM also provides OpenAI-compatible serving endpoints.

### 2.5 Streaming

Streaming sends generated output in chunks rather than waiting
for the entire answer.

It can reduce the time before the user sees the first output.
It does not necessarily reduce total generation time.

### 2.6 KV Cache

The key-value cache stores attention information for previous
tokens during generation. It avoids recomputing some information
at each generation step.

Longer contexts generally require more cache memory. The exact
amount depends on model architecture, cache precision and runtime.

### 2.7 GPU Memory and Runtime

GPU memory is used for model weights, KV cache and temporary
computations when inference runs on a GPU.

A small model may run on a CPU or GPU, depending on available
hardware and configuration. Actual memory usage must be measured
rather than inferred from model-file size alone.

### 2.8 Batching and Continuous Batching

Batching processes multiple requests together.

Continuous batching dynamically adds and removes requests while
generation is running. It can improve throughput for multiple
concurrent users.

### 2.9 TTFT, TPOT and P95 Latency

- TTFT: time to first token.
- TPOT: average time per output token after generation begins.
- P95 latency: the latency below which 95% of measured requests fall.

These metrics help evaluate responsiveness and performance.
Measurements depend on hardware, prompt length, output length,
concurrency and runtime settings.

## 3. Ollama versus vLLM

| Comparison | Ollama | vLLM |
|---|---|---|
| Main use | Local model running and development | High-throughput model serving |
| Setup | Simple local installation | More serving configuration |
| API | Ollama API and supported compatibility endpoints | OpenAI-compatible API |
| Concurrent requests | Suitable for local applications; behavior depends on configuration | Designed for efficient concurrent serving |
| Memory management | Runtime-dependent model and cache management | PagedAttention and serving optimizations |
| Batching | Runtime-dependent | Continuous batching support |
| Best fit | Personal or small local assistants | Production-oriented serving workloads |
| Limitation | Large-scale concurrency may require additional tuning | Hardware and deployment requirements can be more demanding |

## 4. Minimal Implementation

The project includes:

- `Modelfile`: defines the custom model configuration.
- `model_api_test.py`: compares streaming and non-streaming requests.
- `modelfile_test.py`: inspects the custom model configuration.

The model is created with:

`ollama create farm-assist -f .\Day_5_Task\Modelfile`

The custom model can be tested with:

`ollama run farm-assist "How can I reduce water waste on a small farm?"`

The REST API test records response time, token counts and
generation speed when those metrics are returned by Ollama.

## 5. Observations

Record actual results after running the experiments.

- Model build result: [Record actual result]
- Modelfile verification: [Record actual result]
- Non-streaming total time: [Record measured result]
- Streaming time to first output: [Record measured result]
- Generated token count: [Record measured result]
- Generation speed: [Record measured result]
- Errors or limitations: [Record actual observations]

Do not invent benchmark values. Repeat requests under comparable
conditions before drawing performance conclusions.

## 6. Suitability Analysis

Ollama is suitable for this scenario because the application uses
a single local model with a custom system prompt and simple API calls.

vLLM may be a better option when a deployment requires high
throughput, efficient concurrent requests and production-oriented
serving features, provided the hardware and deployment environment
are suitable.

For this local agriculture assistant, Ollama is the initial choice.
A move to vLLM should be considered if measured traffic and
performance requirements justify the additional setup.

## 7. Conclusion

This project demonstrates how a Modelfile customizes a model,
how a Python client communicates with the Ollama REST API, and
how streaming can deliver generated text incrementally.

The comparison also highlights the difference between a simple
local model runner and a serving engine designed for higher
throughput. The final deployment decision should be based on
measured performance, memory constraints and concurrency needs.

## 8. Screenshots

Save actual screenshots of:

1. Successful custom model creation.
2. A response from `farm-assist`.
3. Streaming and non-streaming API test output.
4. Modelfile verification output.

Place these files inside the `screenshots/` directory.
