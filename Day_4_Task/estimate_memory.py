
"""
Day 4 Task: LLM Memory Estimator
Estimates model weights, KV cache, and total memory.
All values are estimates, not measured usage.
"""

import csv
from pathlib import Path

# Example model configuration: 8B-parameter model
PARAMETERS_B = 8
LAYERS = 32
KV_HEADS = 8
HEAD_DIM = 128
BYTES_PER_CACHE_VALUE = 2  # FP16 KV cache
BATCH_SIZE = 1

# Approximate effective bits per parameter, including some overhead
QUANTIZATION = {
    "Q4": 4.5,
    "Q8": 8.5,
    "FP16": 16
}

# Your computer's available physical RAM
SYSTEM_RAM_GB = 15.82

# Context lengths to compare
CONTEXT_LENGTHS = [2048, 4096, 8192, 16384]


def estimate_weights(parameters_b, bits_per_parameter):
    parameters = parameters_b * 1_000_000_000
    weight_bytes = parameters * bits_per_parameter / 8
    return weight_bytes / (1024 ** 3)


def estimate_kv_cache(layers, kv_heads, head_dim,
                      context, bytes_per_value, batch_size):
    # K and V are both stored
    total_bytes = (
        2 * layers * kv_heads * head_dim
        * context * bytes_per_value * batch_size
    )
    return total_bytes / (1024 ** 3)


def main():
    results = []

    print("=" * 72)
    print("DAY 4 TASK: MODEL MEMORY ESTIMATION")
    print("=" * 72)
    print(f"Model parameters: {PARAMETERS_B} billion")
    print(f"System RAM: {SYSTEM_RAM_GB:.2f} GB")
    print("Note: Actual memory also depends on runtime overhead.\n")

    for quant_name, bits in QUANTIZATION.items():
        weights_gb = estimate_weights(PARAMETERS_B, bits)

        for context in CONTEXT_LENGTHS:
            kv_gb = estimate_kv_cache(
                LAYERS,
                KV_HEADS,
                HEAD_DIM,
                context,
                BYTES_PER_CACHE_VALUE,
                BATCH_SIZE
            )

            total_gb = weights_gb + kv_gb

            # Leave 2 GB as a rough allowance for OS and other programs
            usable_ram_gb = SYSTEM_RAM_GB - 2
            fits = total_gb <= usable_ram_gb

            row = {
                "Quantization": quant_name,
                "Context_Tokens": context,
                "Weights_GB": round(weights_gb, 3),
                "KV_Cache_GB": round(kv_gb, 3),
                "Estimated_Total_GB": round(total_gb, 3),
                "Fits_15.82GB_RAM": "Likely" if fits else "Unlikely"
            }
            results.append(row)

            print(
                f"{quant_name:5} | Context: {context:5} | "
                f"Weights: {weights_gb:6.2f} GB | "
                f"KV: {kv_gb:5.2f} GB | "
                f"Total: {total_gb:6.2f} GB | "
                f"{row['Fits_15.82GB_RAM']}"
            )

    output_dir = Path(__file__).resolve().parent / "Output"
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "memory_estimates.csv"

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    print("\nResults saved to:", csv_path)
    print("These are theoretical estimates, not measured model usage.")


if __name__ == "__main__":
    main()
