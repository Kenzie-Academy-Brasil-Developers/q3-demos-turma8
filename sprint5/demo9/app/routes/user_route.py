from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint("users", __name__, url_prefix="/users")


bp.post("")(user_controller.create_user)
bp.get("/<int:user_id>")(user_controller.retrieve_by_id)
bp.get("/<int:user_id>/orders")(user_controller.retrieve_user_orders)
bp.get("/<int:user_id>/invoices")(user_controller.retrieve_user_invoices)
