import json
import os

def get_history_path(username):
    return os.path.join("data", "history", f"{username}.json")

def load_history(username):
    path = get_history_path(username)
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []

def save_history(username, history):
    path = get_history_path(username)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(history, f, indent=4)
