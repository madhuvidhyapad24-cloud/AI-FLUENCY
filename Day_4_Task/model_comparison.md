
# Day 4 Task: Open-Weight Model Comparison

## 1. Scenario

The scenario is a local AI assistant running on a Windows computer
with 15.82 GB of physical RAM.

The assistant should answer questions, summarize text, and support
small coding tasks. The model should fit available memory, support
a useful context length, and have a licence suitable for the intended
use.

## 2. Model Comparison

| Feature | Qwen2.5-7B-Instruct | Llama 3.1 8B Instruct | Mistral-7B-Instruct-v0.3 |
|---|---|---|---|
| Model family | Qwen | Llama | Mistral |
| Parameters | 7.61B | 8B | 7B |
| Published context | Up to 131,072 tokens, with configuration requirements for extended context | 128K tokens | 32K tokens |
| Licence | Apache 2.0 | Llama 3.1 Community Licence | Apache 2.0 |
| Commercial use | Generally permitted under Apache 2.0, subject to its terms | Conditional; review Meta's licence and acceptable-use policy | Generally permitted under Apache 2.0, subject to its terms |
| Ollama tag to investigate | qwen2.5:7b | llama3.1:8b | mistral:7b |
| Local memory | Depends on quantization and context | Depends on quantization and context | Depends on quantization and context |

## 3. Official References

1. Qwen2.5-7B-Instruct:
   https://huggingface.co/Qwen/Qwen2.5-7B-Instruct

2. Llama 3.1:
   https://github.com/meta-llama/llama-models

3. Mistral-7B-Instruct-v0.3:
   https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3

4. Ollama model library:
   https://ollama.com/library

## 4. Licence Analysis

Apache 2.0 permits commercial use, modification, and redistribution
subject to its conditions, including applicable notices and licence
terms.

The Llama 3.1 Community Licence has additional conditions and an
acceptable-use policy. Commercial use is not an unrestricted
permission; users must check the current terms and applicable
thresholds before deployment.

A model being open-weight does not automatically mean that it is
open-source under every definition or free of usage restrictions.

## 5. Memory Suitability

The computer has 15.82 GB of physical RAM, but Windows and other
applications also need memory.

A quantized 7B or 8B model may be a practical local candidate at a
moderate context length. The actual model file size, KV cache,
runtime overhead, and available memory must be checked before
claiming that it fits.

Theoretical memory estimates are not the same as measurements from
a running model.

## 6. Preliminary Recommendation

Qwen2.5-7B-Instruct is a candidate for the local assistant because
it supports multilingual tasks and has an Apache 2.0 licence.
Mistral-7B-Instruct-v0.3 is another Apache 2.0 candidate.
Llama 3.1 8B Instruct is worth comparing for its long context, but
its licence conditions must be considered.

The final choice will be made after testing the selected quantized
model and recording actual memory and runtime observations.
