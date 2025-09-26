# users_db.py
import json
from pathlib import Path

DB_PATH = Path(__file__).parent / "users.json"

def load_users():
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text())
    users = {
        "1": {"id": 1, "name": "Tanisha", "email": "tanisha@example.com"},
        "2": {"id": 2, "name": "Shivani", "email": "shivani@example.com"}
    }
    save_users(users)
    return users

def save_users(users):
    DB_PATH.write_text(json.dumps(users, indent=2))
