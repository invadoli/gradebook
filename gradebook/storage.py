import json
import os
import logging

os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

DEFAULT_PATH = "data/gradebook.json"

def save_data(data, path=DEFAULT_PATH):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        logging.info(f"Successfully saved data to {path}")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        raise

def load_data(path=DEFAULT_PATH):
    try:
        if not os.path.exists(path):
            logging.info(f"Storage file {path} not found. Returning empty structure.")
            return {"students": [], "courses": [], "enrollments": []}
            
        with open(path, 'r') as f:
            data = json.load(f)
            logging.info(f"Successfully loaded data from {path}")
            return data
    except json.JSONDecodeError as e:
        logging.error(f"Corrupted JSON file at {path}: {e}")
        print("A helpful message: The storage file is corrupted. Starting empty.")
        return {"students": [], "courses": [], "enrollments": []}
    except Exception as e:
        logging.error(f"Unexpected error during load: {e}")
        return {"students": [], "courses": [], "enrollments": []}