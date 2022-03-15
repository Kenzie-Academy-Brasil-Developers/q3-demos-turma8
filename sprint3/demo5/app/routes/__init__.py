from app.routes.home_route import home_route
from app.routes.dev_route import dev_route


def init_app(app):
    home_route(app)
    dev_route(app)
