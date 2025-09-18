from flask import Blueprint, request, jsonify
from models import Student, db

student_bp = Blueprint("students", __name__, url_prefix="/students")


@student_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])


@student_bp.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())


@student_bp.route("/", methods=["POST"])
def create_student():
    data = request.get_json()
    student = Student(name=data["name"])
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201


@student_bp.route("/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data.get("name", student.name)
    db.session.commit()
    return jsonify(student.to_dict())


@student_bp.route("/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted"})
