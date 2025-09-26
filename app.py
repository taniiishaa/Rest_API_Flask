# app.py
from flask import Flask, request, jsonify
from users_db import load_users, save_users

app = Flask(__name__)
users = load_users()  # our "database"

def next_id():
    if not users:
        return 1
    return max(int(k) for k in users.keys()) + 1

@app.route("/")
def home():
    return jsonify({"message": "Welcome! Use /users to manage users."})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(list(users.values()))

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(str(user_id))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "name and email are required"}), 400

    uid = next_id()
    user = {"id": uid, "name": data["name"], "email": data["email"]}
    users[str(uid)] = user
    save_users(users)
    return jsonify(user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json() or {}
    key = str(user_id)
    if key not in users:
        return jsonify({"error": "User not found"}), 404

    if "name" in data:
        users[key]["name"] = data["name"]
    if "email" in data:
        users[key]["email"] = data["email"]

    save_users(users)
    return jsonify(users[key])

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    key = str(user_id)
    if key not in users:
        return jsonify({"error": "User not found"}), 404
    del users[key]
    save_users(users)
    return jsonify({"message": f"User {user_id} deleted."})

if __name__ == "__main__":
    app.run(debug=True)
