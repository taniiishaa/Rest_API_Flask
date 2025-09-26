📌 Task Summary
- This repository contains a Python-based Flask API for managing user data with full CRUD (Create, Read, Update, Delete) functionality.
- The project was part of my internship tasks and demonstrates API development, JSON handling, HTTP requests, and testing using Postman.

🚀 My Development Process
1. Project Planning & Breakdown
- Defined the objective: Create a RESTful API to manage users and demonstrate CRUD operations.
- Chose Python + Flask for simplicity and rapid backend development.
- Planned to include:
a. Create, Read, Update, Delete operations for users
b. In-memory data storage for simplicity
c. JSON-based request and response format

2. Core Implementation
- Built a Flask server with routes for /users (GET, POST) and /users/<id> (PUT, DELETE).
- Stored users in a list of dictionaries with id, name, and email.
- Used request.get_json() to handle JSON input from the client.
- Returned JSON responses for all operations.

3. Extra Touches for Professional Look
- Included clear success and error messages in JSON responses.
- Made API easily testable with Postman.
- Structured code for readability and scalability (easy to replace in-memory storage with a database later).

📖 Application Description
- This Flask API allows users to Create, Read, Update, and Delete user records.
- It demonstrates:
    a. RESTful API design with Flask
    b. Handling JSON requests and responses
    c. Implementing CRUD operations
    d. Testing APIs with Postman

✨ Key Features
- Get All Users: Fetch all existing users.
- Add User: Add a new user with name and email.
- Update User: Update user details by id.
- Delete User: Remove a user by id.
- JSON Responses: Clear, structured output for each request.
- Easy Testing: Fully testable via Postman without needing a database.

⚙️ Technologies Used
- Language: Python 3.13
- Framework: Flask
- Tools: VS Code / Terminal / Postman
- Libraries: flask, jsonify, request

🎯 Outcome
- This project resulted in a fully functional, testable Flask API demonstrating:
- Building RESTful endpoints with Python
- Handling CRUD operations using JSON
- Using Postman to interact with and validate APIs
- Structuring code for clarity and future enhancements
