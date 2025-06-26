import requests
import json

# Load your ID token from the login step
with open("login/hydros_tokens.json") as f:
    tokens = json.load(f)

headers = {
    "authorization": tokens["id_token"]
}

# Get all user data (includes devices)
resp = requests.get("https://cv.hydros.link/user", headers=headers)
resp.raise_for_status()
user_json = resp.json()

# Print ALL devices in a readable format
print("\nYour Hydros devices:\n")
for device in user_json.get("things", []):
    print(
        f"- thingName: {device['thingName']}\n"
        f"  friendlyName: {device.get('friendlyName')}\n"
        f"  thingType: {device.get('thingType')}\n"
        f"  status: {'Online' if device.get('connectionStatus') else 'Offline'}"
    )
    print()

# Optionally, save as JSON for reference
with open("hydros_devices.json", "w") as f:
    json.dump(user_json["things"], f, indent=2)
