# Day 4 Task: Will It Fit, and May I Use It?

## Project Overview

This project investigates whether a language model can run within the memory limits of a local computer. It explores model-weight memory, quantization, KV cache, context length, and model licensing.

The experiments combine theoretical memory estimation with a comparison of open-weight models and their licence conditions.

## Objectives

- Estimate model-weight memory requirements.
- Understand the role of the KV cache during inference.
- Compare Q4, Q8, and FP16 precision assumptions.
- Evaluate how context length affects estimated memory usage.
- Compare model specifications and licence conditions.
- Identify suitable candidates for local inference.

## Hardware and Environment

- Operating system: Windows
- Physical RAM: 15.82 GB
- Model runner: Ollama
- Python environment: Virtual environment (`.venv`)

**Note:** No Ollama models were installed at the initial inspection. Actual inference measurements must be recorded after a model runs successfully.

## Technologies Used

- Python
- Ollama
- CSV for experiment results
- Markdown for documentation
- VS Code
- Git and GitHub

## Project Structure

```text
Day_4_Task/
├── estimate_memory.py
├── context_quantization.py
├── model_comparison.md
├── analysis.md
├── README.md
├── Output/
│   ├── memory_estimates.csv
│   └── context_quantization.csv
└── screenshots/
```

## Experiments

### 1. Memory Estimation

`estimate_memory.py` estimates model-weight memory, KV-cache memory, and total memory for different quantization assumptions and context lengths.

### 2. Context Length and Quantization

`context_quantization.py` compares Q4 and Q8 weight assumptions across multiple context lengths.

The results are saved as CSV files in the `Output/` directory.

### 3. Model and Licence Comparison

`model_comparison.md` compares Qwen2.5-7B-Instruct, Llama 3.1 8B Instruct, and Mistral-7B-Instruct-v0.3.

It discusses model size, context length, licence conditions, commercial-use considerations, and suitability for local inference.

### 4. Analysis Report

`analysis.md` explains memory concepts, quantization, context length, experimental limitations, suitability, and conclusions.

## How to Run

From the main project directory, run:

```powershell
python .\Day_4_Task\estimate_memory.py
python .\Day_4_Task\context_quantization.py
```

These scripts do not require an installed language model because they calculate theoretical estimates.

## Important Limitations

- Memory calculations are estimates, not measurements from a running model.
- Actual usage depends on the model architecture, quantization format, runtime, context configuration, and other applications.
- Published model context limits may require specific configurations.
- Open-weight availability does not automatically mean unrestricted commercial use.
- Licence terms should be checked on the official model page before deployment.

## Official References

- Qwen: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- Meta Llama: https://github.com/meta-llama/llama-models
- Mistral: https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
- Ollama model library: https://ollama.com/library

## Conclusion

This project demonstrates how model size, quantization, context length, and KV-cache requirements influence local inference feasibility.

The final model choice should balance memory requirements, response quality, runtime performance, context needs, and licence conditions.

**Project:** Day 4 – AI Fluency Assessment
