import json
import os

DEFAULT_PATH = "data/gradebook.json"

def save_data(data, path=DEFAULT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_data(path=DEFAULT_PATH):
    """Loads data from JSON. Handles missing or corrupted files."""
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"students": [], "courses": [], "enrollments": []}
    except json.JSONDecodeError:
        print(f"ERROR: The file at {path} contains invalid JSON. Starting fresh.")
        return {"students": [], "courses": [], "enrollments": []}