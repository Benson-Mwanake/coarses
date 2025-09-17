from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

enrollments = db.Table(
    "enrollments",
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)


class Course(db.Model, SerializerMixin):
    _tablename_ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    credits = db.Column(db.Integer, default=3)

    students = db.relationship(
        "Student", secondary=enrollments, back_populates="courses"
    )

    def _repr_(self):
        return f"<Course {self.name}>"


class Student(db.Model, SerializerMixin):
    _tablename_ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    courses = db.relationship(
        "Course", secondary=enrollments, back_populates="students"
    )

    def _repr_(self):
        return f"<Student {self.name}>"
