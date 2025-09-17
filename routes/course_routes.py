rom flask import Blueprint, request, jsonify
from models import db, Course

course_bp = Blueprint("courses", _name_, url_prefix="/courses")

@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([c.to_dict() for c in courses]), 200

@course_bp.route("/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict()), 200

@course_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Course name is required"}), 400

    new_course = Course(
        name=data["name"],
        description=data.get("description"),
        credits=data.get("credits", 3)
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify(new_course.to_dict()), 201

@course_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()

    course.name = data.get("name", course.name)
    course.description = data.get("description", course.description)
    course.credits = data.get("credits", course.credits)

    db.session.commit()
    return jsonify(course.to_dict()), 200

@course_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully"}), 200