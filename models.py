from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


class Course(db.Model, SerializerMixin):
    __tablename__ = "courses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer, default=3)

    students = db.relationship(
        "Student", secondary="enrollments", back_populates="courses"
    )

    def __repr__(self):
        return f"<Course {self.name}>"


class Student(db.Model, SerializerMixin):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    courses = db.relationship(
        "Course", secondary="enrollments", back_populates="students"
    )

    def __repr__(self):
        return f"<Student {self.name}>"


enrollments = db.Table(
    "enrollments",
    db.Column("student_id", db.Integer, db.ForeignKey("students.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("courses.id"), primary_key=True),
)
