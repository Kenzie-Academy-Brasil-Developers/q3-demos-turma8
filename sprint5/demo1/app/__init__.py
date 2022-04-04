from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://chan:1234@localhost:5432/sprint5_demo1"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.models.call_record_model import CallRecord

    # with app.app_context():
    #     db.create_all()

    # db.create_all()
    db.create_all(app=app)
    # db.drop_all()

    return app
