from flask import Flask, Blueprint
from app.controller import user_controller

bp = Blueprint("users", __name__, url_prefix="/api")


# def user_route(app: Flask):
#     # @app.get("/users")
#     # def retrieve():
#     #     return {"msg": "Rota de busca de usuarios"}
#     ...
# app.get("/users")(user_controller.get_users)

# @bp.get("/users")
# def retrieve():
#     return user_controller.get_users()


bp.get("/users")(user_controller.get_users)
bp.get("/users/<user_id>")(user_controller.get_user_by_id)
# bp.post("/users")(user_controller.create_user)
