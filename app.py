from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Example route
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the backend!"

@app.route("/students", methods=["GET"])
def get_students():
    # Dummy data for students
    students = [
        {"id": 1, "name": "John Doe", "score": 95},
        {"id": 2, "name": "Jane Smith", "score": 89},
    ]
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensure it binds to 0.0.0.0
