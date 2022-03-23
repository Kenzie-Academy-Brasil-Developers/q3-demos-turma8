from flask import Flask

# from .user_route import user_route
from .product_route import product_route

from .user_route import bp as bp_user


def init_app(app: Flask):
    # user_route(app)
    product_route(app)

    app.register_blueprint(bp_user)
