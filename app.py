from flask import Flask
from models import db
from routes.course_routes import course_bp
from routes.student_routes import student_bp


def create_app():
    app = Flask(_name_)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///courses.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(course_bp)
    app.register_blueprint(student_bp)

    with app.app_context():
        db.create_all()

    return app


if _name_ == "_main_":
    app = create_app()
    app.run(debug=True)
