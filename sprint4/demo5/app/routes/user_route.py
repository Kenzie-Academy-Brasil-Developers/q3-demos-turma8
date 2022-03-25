from flask import Blueprint
from app.controller import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")

bp.get("")(user_controller.get_users)
bp.post("")(user_controller.add_user)
bp.get("/<user_id>")(user_controller.get_user_by_id)
bp.patch("/<user_id>")(user_controller.update_user)
