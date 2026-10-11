
# Day 4 Task: Model Memory, Quantization, Context and Licences

## 1. Objective

The objective is to estimate whether a language model can fit the
available computer memory, understand quantization and context-length
trade-offs, and compare model licences for a local AI assistant.

## 2. Hardware and Environment

- Operating system: Windows
- Physical RAM: 15.82 GB
- Model runner: Ollama
- Ollama client version: 0.35.1
- Installed Ollama models at initial inspection: None
- Memory estimates: Python scripts in this project

Ollama initially reported that it could not connect to a running
instance. No model execution result should be claimed until the
Ollama server is running and a model has been tested.

## 3. Memory Concepts

### 3.1 Model Weight Memory

Model weights store the learned parameters of a model.

A simplified estimate is:

Weight memory in bytes =
Number of parameters × Bits per parameter / 8

For an illustrative 8-billion-parameter model:

- At 4 bits per parameter, the raw weight estimate is about 3.73 GiB.
- At 8 bits per parameter, the raw weight estimate is about 7.45 GiB.
- At 16 bits per parameter, the raw weight estimate is about 14.90 GiB.

These raw estimates exclude quantization metadata, alignment,
runtime overhead and other memory requirements. The Python estimator
uses effective bits per parameter to approximate some overhead.

### 3.2 KV Cache Memory

The key-value cache stores attention information for previously
processed tokens during inference.

For a conventional transformer architecture, a simplified estimate is:

KV cache bytes =
2 × Layers × KV heads × Head dimension
× Context tokens × Bytes per cache value × Batch size

The factor of two represents keys and values.

Actual cache usage depends on the model architecture, cache
precision, implementation and batch size.

### 3.3 Runtime and Available Memory

Total inference memory includes model weights, KV cache, temporary
working memory, runtime overhead and other allocations.

The computer has 15.82 GB of physical RAM. Not all of this is
available to the model because Windows and other applications
also consume memory.

## 4. Quantization

Quantization stores model weights using fewer bits.

- Q4: generally uses less weight memory, but may reduce quality
  depending on the model and quantization method.
- Q8: generally uses more weight memory and may preserve more
  numerical precision than a comparable Q4 variant.
- FP16: uses 16-bit floating-point values and typically requires
  substantially more weight memory.

Quantization does not guarantee a specific quality level.
Performance and quality should be evaluated using the selected
model and quantization format.

## 5. Context Length

Context length is the number of tokens a model can process in its
context window.

A longer context can accommodate more input and conversation
history, but it may increase KV-cache memory and processing cost.

The theoretical experiment compares contexts of 2,048, 4,096,
8,192 and 16,384 tokens.

The configured context length is not necessarily the same as the
maximum context supported by the published model.

## 6. Experiment Results

### 6.1 Memory Estimation

The estimator uses an illustrative 8B model configuration.

Refer to `Output/memory_estimates.csv` for the generated results.

These results are theoretical estimates, not measurements of a
real model running in Ollama.

### 6.2 Context and Quantization Comparison

Refer to `Output/context_quantization.csv`.

Record the main observations after running the scripts:

- How weight memory changes between Q4 and Q8.
- How KV-cache memory changes with context length.
- Which configurations are estimated to fit within the chosen
  memory budget.
- Why actual runtime memory can differ from estimates.

### 6.3 Actual Model Test

Complete this section only after a model runs successfully.

- Model and exact tag: [Record actual model]
- Quantization: [Record actual quantization]
- Configured context length: [Record actual setting]
- Observed memory use: [Record measurement, if available]
- Test result: [Record actual result]
- Limitations: [Record errors or observations]

Do not substitute theoretical estimates for measured values.

## 7. Open-Weight Model and Licence Comparison

The models considered are:

1. Qwen2.5-7B-Instruct
2. Llama 3.1 8B Instruct
3. Mistral-7B-Instruct-v0.3

Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 use Apache 2.0
licensing. Llama 3.1 uses Meta's Llama 3.1 Community Licence.

Apache 2.0 generally permits commercial use subject to its terms.
The Llama licence has additional conditions and an acceptable-use
policy. Review the current official licence before deployment.

Official references:

- https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
- https://github.com/meta-llama/llama-models
- https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
- https://ollama.com/library

## 8. Suitability Analysis

For a computer with 15.82 GB RAM, a quantized model in the 7B range
is a reasonable candidate for testing. A moderate context length
may be more practical than a very long one.

The final choice should consider:

- Memory usage and available headroom.
- Response quality for the intended tasks.
- Context length requirements.
- Inference speed.
- Licence conditions and intended use.
- Actual compatibility with the installed runtime.

A model should not be declared suitable solely because its
estimated weight memory fits within physical RAM.

## 9. Conclusion

This experiment illustrates how parameter count, quantization,
context length and runtime overhead affect local language-model
memory requirements.

It also shows that model selection involves more than technical
performance. Licence conditions and the intended use must be
considered before choosing a model for deployment.

The final recommendation should be based on the memory estimates,
verified licence terms and actual model tests.
