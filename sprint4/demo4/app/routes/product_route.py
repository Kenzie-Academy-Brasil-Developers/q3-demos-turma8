from flask import Blueprint
from app.controller import product_controller

bp = Blueprint("products", __name__, url_prefix="/products")


bp.get("")(product_controller.get_products)
