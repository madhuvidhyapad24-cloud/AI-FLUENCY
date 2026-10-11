# Day 5 Task: Serving Models Your Way

## Project Overview

This project demonstrates how to serve a customized language model using Ollama, a Modelfile, and the REST API. It uses a smart-agriculture assistant called **FarmAssist** as the example scenario.

The project also discusses when a local model runner such as Ollama is suitable and when a serving engine such as vLLM may be preferable.

## Objectives

- Create a custom Ollama model using a Modelfile.
- Configure a system prompt, temperature, and context length.
- Send non-streaming and streaming requests through the Ollama REST API.
- Measure response time and token-generation metrics.
- Compare Ollama with vLLM.
- Document observations and limitations.

## Technologies Used

- Python
- Ollama
- Qwen2.5 3B
- Ollama REST API
- JSON and HTTP
- VS Code
- Git and GitHub

## Project Structure

```text
Day_5_Task/
├── Modelfile
├── model_api_test.py
├── modelfile_test.py
├── analysis.md
├── README.md
├── Output/
└── screenshots/
```

## Scenario: FarmAssist

FarmAssist provides general smart-agriculture guidance. Its system prompt encourages practical answers and instructs the model not to invent current weather or sensor readings.

## Setup

Download the base model:

```powershell
ollama pull qwen2.5:3b
```

Build the custom model:

```powershell
ollama create farm-assist -f .\Day_5_Task\Modelfile
```

Test it:

```powershell
ollama run farm-assist "How can I reduce water waste on a small farm?"
```

## Run the Experiments

Test streaming and non-streaming requests:

```powershell
python .\Day_5_Task\model_api_test.py
```

Inspect the custom model configuration:

```powershell
python .\Day_5_Task\modelfile_test.py
```

Ensure the Ollama service is running before executing the Python scripts.

## Performance Metrics

The API experiment records available metrics such as:

- Total response time
- Time to first output for streaming
- Prompt and generated token counts
- Generation speed in tokens per second

Record actual results from your own execution. Performance depends on hardware, prompt length, model settings, and runtime conditions.

## Ollama versus vLLM

Ollama is convenient for running models locally and developing small applications. vLLM offers serving optimizations such as continuous batching and PagedAttention, making it a candidate for workloads with higher concurrency and throughput requirements.

The appropriate choice depends on deployment needs and measured performance.

## Limitations

- Model responses can be incorrect and should be validated.
- Streaming improves incremental delivery but does not guarantee lower total response time.
- Results from a single request are insufficient for a reliable performance comparison.
- The vLLM comparison is conceptual unless vLLM is actually installed and tested.

## Conclusion

This project demonstrates local model customization, REST API integration, streaming, and basic performance measurement. It compares two serving approaches and explains how to select an approach based on memory, responsiveness, and concurrency requirements.

**Project:** Day 5 – AI Fluency Assessment
