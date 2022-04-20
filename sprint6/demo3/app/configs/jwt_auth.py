from flask_jwt_extended import JWTManager
import os

# jwt = JWTManager()


def init_app(app):
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET')
    # jwt.init_app(app)
    JWTManager(app)
