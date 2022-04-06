from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Singleton
db = SQLAlchemy()


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    # app.batata = "Batata"
    # print(f"{app.batata=}")

    from app.models.call_record_model import CallRecord

    # db.create_all(app=app)
