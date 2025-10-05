# 🛡️ RESTful Microservice Prototype: User Resource Management

[![Project Status](https://img.shields.io/badge/Status-Complete%20%7C%20RESTful%20CRUD-009688?style=for-the-badge)](./app.py)
[![Framework](https://img.shields.io/badge/Framework-Python%20Flask-263238?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Focus](https://img.shields.io/badge/Focus-Architecture%20%7C%20Stateless%20Design-1565c0?style=for-the-badge)]()

---

## 💡 Project Overview: Foundational Backend Architecture

This repository contains a high-fidelity prototype of a **microservice** designed exclusively for **User Resource Management**. It demonstrates a core competency in constructing a reliable, scalable backend by strictly adhering to **RESTful architectural principles** using Python and the Flask framework.

The primary objective was to implement a full **CRUD (Create, Read, Update, Delete)** data lifecycle within a clean, testable environment, ready to be scaled with minimal effort.

## 🛠️ Engineering Disciplines Demonstrated

This project showcases expertise in several crucial backend development areas:

### 1. **RESTful Contract Adherence and Status Management**
* **Semantic Routing:** The API maps HTTP verbs (GET, POST, PUT, DELETE) directly and exclusively to their intended resource operations, ensuring full compliance with the REST standard.
* **Precise Error Reporting:** Returns the specific and necessary HTTP status codes: **`201 Created`** on successful resource generation, **`404 Not Found`** for missing resources, and **`400 Bad Request`** upon invalid JSON payload/missing fields.

### 2. **Architecture and Scalability**
* **Separation of Concerns (SoC):** The logic is strictly partitioned into **Application Logic** (`app.py`, handling routing and request processing) and **Persistence Logic** (`users_db.py`, handling I/O). This clean abstraction makes the system database-agnostic.
* **Stateless Processing:** The Flask application itself holds no persistent state, relying entirely on the I/O handler. This architecture is crucial for microservices, allowing the service to be easily **load-balanced and scaled horizontally** without session issues.

### 3. **Data Integrity and Mutability Control**
* **Atomic JSON Persistence:** The `save_users` function ensures that any mutation (Create, Update, Delete) is immediately and completely written to the JSON "database," maintaining data consistency.
* **Robust ID Generation:** Implements dynamic auto-incrementing ID logic (`next_id()`) by checking the current maximum key, preventing ID collisions even after deletions or system restarts.

---

## ⚙️ Application Structure

The service is comprised of two Python files and one JSON persistence file:

| File/Variable | Purpose | Engineering Highlight |
| :--- | :--- | :--- |
| `app.py` | Core Flask application and routing. | Manages all API endpoints and request/response serialization. |
| `users_db.py` | Data persistence and I/O handler. | Abstraction layer for data access, currently using JSON file storage. |
| `users.json` | The flat-file "database." | Demonstrates non-volatile storage and state retention between runs. |
| `next_id()` | ID generation utility. | Handles the automatic and safe assignment of new unique user IDs. |

## 🚀 Quick Setup

This application requires only Python 3.x and the Flask library.

1. **Install Dependencies:**
   ```bash
   pip install Flask
   ```
2. **Execute the Microservice:**
   ```bash
   python app.py
   ```
The microservice will be operational at: http://127.0.0.1:5000/

## 🎯 Outcome

This project validates my ability to design and implement a production-ready RESTful API contract, focusing on architectural scalability, code modularity, and strict adherence to professional backend standards—essential skills for any high-growth engineering team.
