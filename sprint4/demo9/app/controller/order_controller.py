from http import HTTPStatus
from flask import jsonify
from app.models.order_model import Order


def get_orders():
    orders = Order.select_all()

    serialized_orders = [Order.serialize(order) for order in orders]

    return jsonify(serialized_orders), HTTPStatus.OK


def get_order_by(order_id: str):
    user_order_info = Order.get_order_user_info(order_id)
    products = Order.get_order_products(order_id)

    user_order_info.update({"products": products})

    print(f"{user_order_info=}")

    return jsonify(user_order_info), HTTPStatus.OK
