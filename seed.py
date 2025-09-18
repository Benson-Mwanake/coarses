from app import create_app
from models import db, Course, Student

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    courses = [
        Course(name="Math 101", description="Intro to Algebra", credits=4),
        Course(name="History 201", description="World History Overview", credits=3),
        Course(name="CS 301", description="Data Structures", credits=5),
    ]

    students = [
        Student(name="Alice"),
        Student(name="Bob"),
        Student(name="Charlie"),
    ]

    db.session.add_all(courses + students)
    db.session.commit()

    print("✅ Database seeded with sample courses & students!")
