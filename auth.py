import json
import os
import hashlib

USERS_FILE = "users.json"

def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def signup(email, password):
    users = load_users()
    if email in users:
        return False
    users[email] = {"password": hash_password(password), "history": []}
    save_users(users)
    return True

def login(email, password):
    users = load_users()
    hashed = hash_password(password)
    return email in users and users[email]["password"] == hashed

def save_history(email, history):
    users = load_users()
    if email in users:
        users[email]["history"].append(history)
        save_users(users)

def get_history(email):
    users = load_users()
    if email in users:
        return users[email]["history"]
    return []
