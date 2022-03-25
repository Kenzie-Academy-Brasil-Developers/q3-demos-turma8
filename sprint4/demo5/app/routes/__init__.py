from flask import Flask, Blueprint

from .product_route import bp as bp_product
from .user_route import bp as bp_user

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_product)

    app.register_blueprint(bp_api)
