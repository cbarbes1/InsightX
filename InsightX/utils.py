import json

def save_json(data, filename="data.json"):
    """Saves data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

