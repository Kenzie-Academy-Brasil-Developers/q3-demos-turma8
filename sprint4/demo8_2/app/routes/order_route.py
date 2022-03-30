from flask import Blueprint
from app.controller import order_controller

bp = Blueprint("orders", __name__, url_prefix="/orders")

bp.get("")(order_controller.get_orders)
