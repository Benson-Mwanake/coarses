from flask import Blueprint, request, jsonify
from models import Course, db

course_bp = Blueprint("courses", __name__, url_prefix="/courses")


@course_bp.route("/", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


@course_bp.route("/<int:id>", methods=["GET"])
def get_course(id):
    course = Course.query.get_or_404(id)
    return jsonify(course.to_dict())


@course_bp.route("/", methods=["POST"])
def create_course():
    data = request.get_json()
    course = Course(
        name=data["name"],
        description=data.get("description"),
        credits=data.get("credits", 3),
    )
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201


@course_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):
    course = Course.query.get_or_404(id)
    data = request.get_json()
    course.name = data.get("name", course.name)
    course.description = data.get("description", course.description)
    course.credits = data.get("credits", course.credits)
    db.session.commit()
    return jsonify(course.to_dict())


@course_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):
    course = Course.query.get_or_404(id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted"})
