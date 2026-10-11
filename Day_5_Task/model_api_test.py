
import json
import time
import urllib.request

API_URL = "http://localhost:11434/api/generate"
MODEL = "farm-assist"

PROMPT = (
    "A farmer has limited water. Give three practical ways "
    "to reduce water waste on a small farm."
)


def generate(stream):
    payload = {
        "model": MODEL,
        "prompt": PROMPT,
        "stream": stream
    }

    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        API_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    start = time.perf_counter()
    response_text = ""
    first_token_time = None

    with urllib.request.urlopen(request, timeout=300) as response:
        if stream:
            for line in response:
                if not line.strip():
                    continue

                item = json.loads(line.decode("utf-8"))

                if item.get("response"):
                    if first_token_time is None:
                        first_token_time = time.perf_counter() - start

                    response_text += item["response"]

                if item.get("done"):
                    final_data = item
        else:
            final_data = json.loads(response.read().decode("utf-8"))
            response_text = final_data.get("response", "")

    elapsed = time.perf_counter() - start

    print("\n" + "=" * 55)
    print("STREAMING:", stream)
    print("RESPONSE:\n", response_text)
    print(f"\nTotal time: {elapsed:.2f} seconds")

    if stream:
        print("Time to first output:",
              f"{first_token_time:.2f} seconds"
              if first_token_time is not None else "No output token")

    print("Prompt tokens:", final_data.get("prompt_eval_count", "N/A"))
    print("Generated tokens:", final_data.get("eval_count", "N/A"))

    token_count = final_data.get("eval_count", 0)
    generation_time = final_data.get("eval_duration", 0) / 1_000_000_000

    if generation_time > 0:
        print(f"Generation speed: {token_count / generation_time:.2f} tokens/sec")


if __name__ == "__main__":
    print("Testing non-streaming response...")
    generate(False)

    print("\nTesting streaming response...")
    generate(True)
