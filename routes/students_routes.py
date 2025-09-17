from flask import Blueprint, request, jsonify
from models import db, Student, Course

student_bp = Blueprint("students", _name_, url_prefix="/students")


@student_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students]), 200


@student_bp.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict()), 200


@student_bp.route("/", methods=["POST"])
def create_student():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    new_student = Student(name=data["name"], email=data["email"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201


@student_bp.route("/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.name = data.get("name", student.name)
    student.email = data.get("email", student.email)

    db.session.commit()
    return jsonify(student.to_dict()), 200


@student_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200


# Extra: Enroll a student in a course
@student_bp.route("/<int:student_id>/enroll/<int:course_id>", methods=["POST"])
def enroll_student(student_id, course_id):
    student = Student.query.get_or_404(student_id)
    course = Course.query.get_or_404(course_id)

    if course in student.courses:
        return jsonify({"message": "Already enrolled"}), 400

    student.courses.append(course)
    db.session.commit()
    return jsonify({"message": f"{student.name} enrolled in {course.name}"}), 200
