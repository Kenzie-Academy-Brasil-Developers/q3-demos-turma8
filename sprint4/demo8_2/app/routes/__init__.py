from flask import Flask, Blueprint

from .product_route import bp as bp_product
from .user_route import bp as bp_user
from .order_route import bp as bp_order

bp_api = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp_api.register_blueprint(bp_user)
    bp_api.register_blueprint(bp_product)
    bp_api.register_blueprint(bp_order)

    app.register_blueprint(bp_api)
