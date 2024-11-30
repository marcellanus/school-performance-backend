from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# Sample data structure to hold student performance data
# In a real-world app, this would be replaced with a database
students = [
    {
        "id": 1,
        "name": "John Doe",
        "subjects": [
            {"name": "Math", "assessment": 80, "exam": 90},
            {"name": "Science", "assessment": 70, "exam": 85}
        ]
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "subjects": [
            {"name": "Math", "assessment": 90, "exam": 95},
            {"name": "Science", "assessment": 85, "exam": 80}
        ]
    }
]

@app.route("/")
def home():
    return "Welcome to the School Performance Website Backend"

@app.route("/students", methods=["GET"])
def get_students():
    students = [
        {"name": "John Doe", "score": 85},
        {"name": "Jane Smith", "score": 90},
        {"name": "Mark Johnson", "score": 78},
    ]
    return jsonify(students)


@app.route("/add_student", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added successfully"}), 201

@app.route("/update_student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student["id"] == student_id:
            student.update(data)
            return jsonify({"message": "Student updated successfully"})
    return jsonify({"error": "Student not found"}), 404

@app.route("/delete_student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    students = [student for student in students if student["id"] != student_id]
    return jsonify({"message": "Student deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
