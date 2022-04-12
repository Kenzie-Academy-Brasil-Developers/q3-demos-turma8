from flask import Blueprint, Flask
from .user_route import bp as bp_user

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)

    app.register_blueprint(bp_api)
