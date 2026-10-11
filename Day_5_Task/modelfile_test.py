
import json
import urllib.request

API_URL = "http://localhost:11434/api/show"
MODEL = "farm-assist"

payload = {"name": MODEL}
data = json.dumps(payload).encode("utf-8")

request = urllib.request.Request(
    API_URL,
    data=data,
    headers={"Content-Type": "application/json"}
)

try:
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))

    print("=" * 60)
    print("DAY 5 TASK - MODELFILE VERIFICATION")
    print("=" * 60)

    print("\nModel:", MODEL)
    print("\nModel details:")
    print(json.dumps(result.get("details", {}), indent=2))

    print("\nModel parameters:")
    print(result.get("parameters", "Not reported"))

    print("\nSystem prompt:")
    print(result.get("system", "Not reported"))

    print("\nModelfile:")
    print(result.get("modelfile", "Not reported"))

except Exception as error:
    print("Could not inspect the model:", error)
    print("Check that Ollama is running and farm-assist exists.")
