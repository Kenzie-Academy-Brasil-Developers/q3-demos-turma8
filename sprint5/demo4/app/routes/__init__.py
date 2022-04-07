from flask import Blueprint, Flask
from app.routes.call_record_route import bp as bp_call

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_call)

    app.register_blueprint(bp_api)
