
"""
Day 4 Task: Context Length and Quantization Experiment

Uses a theoretical memory model. It does not claim to measure
actual Ollama memory usage.
"""

import csv
from pathlib import Path

# Illustrative 8B model architecture
PARAMETERS_B = 8
LAYERS = 32
KV_HEADS = 8
HEAD_DIM = 128
KV_BYTES = 2           # FP16 KV cache
BATCH_SIZE = 1
SYSTEM_RAM_GB = 15.82
OS_RESERVE_GB = 2.0

# Effective bits per parameter, including approximate overhead
QUANTIZATION = {
    "Q4": 4.5,
    "Q8": 8.5,
}

CONTEXT_LENGTHS = [2048, 4096, 8192, 16384]


def weight_memory_gb(parameters_b, bits):
    total_bytes = parameters_b * 1_000_000_000 * bits / 8
    return total_bytes / (1024 ** 3)


def kv_cache_gb(context_length):
    total_bytes = (
        2 * LAYERS * KV_HEADS * HEAD_DIM
        * context_length * KV_BYTES * BATCH_SIZE
    )
    return total_bytes / (1024 ** 3)


def main():
    output_dir = Path(__file__).resolve().parent / "Output"
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = []

    print("=" * 76)
    print("CONTEXT LENGTH AND QUANTIZATION EXPERIMENT")
    print("=" * 76)
    print(f"Illustrative model: {PARAMETERS_B}B parameters")
    print(f"Physical RAM reported: {SYSTEM_RAM_GB:.2f} GB")
    print(f"Estimated RAM available after reserve: "
          f"{SYSTEM_RAM_GB - OS_RESERVE_GB:.2f} GB")
    print("\nAll values are theoretical estimates.\n")

    for quantization, bits in QUANTIZATION.items():
        weights = weight_memory_gb(PARAMETERS_B, bits)

        for context in CONTEXT_LENGTHS:
            cache = kv_cache_gb(context)
            total = weights + cache
            fits = total <= SYSTEM_RAM_GB - OS_RESERVE_GB

            row = {
                "Quantization": quantization,
                "Context_Tokens": context,
                "Weights_GB": round(weights, 3),
                "KV_Cache_GB": round(cache, 3),
                "Estimated_Total_GB": round(total, 3),
                "Estimated_Fit": "Likely" if fits else "Unlikely",
            }
            rows.append(row)

            print(
                f"{quantization:3} | Context {context:5} | "
                f"Weights {weights:6.2f} GB | "
                f"KV cache {cache:5.2f} GB | "
                f"Total {total:6.2f} GB | "
                f"{row['Estimated_Fit']}"
            )

    csv_path = output_dir / "context_quantization.csv"

    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nSaved results:", csv_path)
    print("\nInterpretation:")
    print("- Q4 generally requires less weight memory than Q8.")
    print("- Longer context increases KV-cache memory.")
    print("- Actual memory can differ because of runtime overhead,")
    print("  architecture, GPU offloading and the model file format.")


if __name__ == "__main__":
    main()
