import requests
import json
import time

# Load tokens
with open("login/hydros_tokens.json") as f:
    tokens = json.load(f)

headers = {
    "authorization": tokens["id_token"]
}

# Load device list (from previous script)
with open("hydros_devices.json") as f:
    devices = json.load(f)

for device in devices:
    thing_name = device["thingName"]
    print(f"Pulling /thing/{thing_name} ... ", end="", flush=True)
    try:
        resp = requests.get(f"https://cv.hydros.link/thing/{thing_name}", headers=headers)
        resp.raise_for_status()
        device_meta = resp.json()
        with open(f"hydros_{thing_name}.json", "w") as outf:
            json.dump(device_meta, outf, indent=2)
        print("OK")
    except Exception as e:
        print(f"FAILED: {e}")
    time.sleep(0.5)  # Be nice to the API!

print("\nDONE! Each device's metadata saved as hydros_{thingName}.json")
