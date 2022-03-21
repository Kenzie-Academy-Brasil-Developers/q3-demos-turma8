from flask import Flask

# from app.routes import init_app
from app import routes


# Flask Factory
def create_app():
    app = Flask(__name__)

    # Inicializador de rotas
    routes.init_app(app)

    return app
