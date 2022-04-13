from flask import Blueprint
from app.controllers import order_controller

bp = Blueprint("orders", __name__, url_prefix="/orders")


bp.get("/<int:order_id>")(order_controller.retrieve_by_id)
bp.get("/<int:order_id>/products")(order_controller.order_products)
