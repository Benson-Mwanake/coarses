from app import create_app
from models import db, Course, Student

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    courses = [
        Course(name="Math 101", description="Intro to Algebra", credits=4),
        Course(name="History 201", description="World Civilizations", credits=3),
        Course(
            name="Computer Science 101", description="Basics of Programming", credits=5
        ),
        Course(name="English 101", description="Introduction to Literature", credits=3),
        Course(
            name="Physics 101", description="Mechanics and Thermodynamics", credits=4
        ),
    ]
    db.session.add_all(courses)

    students = [
        Student(name="Alice Johnson", email="alice@example.com"),
        Student(name="Bob Smith", email="bob@example.com"),
        Student(name="Charlie Brown", email="charlie@example.com"),
    ]
    db.session.add_all(students)
    db.session.commit()

    students[0].courses.append(courses[0])
    students[0].courses.append(courses[2])
    students[1].courses.append(courses[1])
    students[1].courses.append(courses[3])
    students[2].courses.extend(courses)

    db.session.commit()

    print("✅ Database seeded with sample courses & students!")
