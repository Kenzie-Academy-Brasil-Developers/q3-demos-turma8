from flask import Flask
from .character_blueprint import bp as bp_char


def init_app(app: Flask):
    app.register_blueprint(bp_char)
