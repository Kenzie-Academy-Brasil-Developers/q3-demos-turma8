from http import HTTPStatus
from flask import jsonify
from app.models.order_model import Order


def get_orders():
    orders = Order.select_all()

    serialized_orders = [Order.serialize(order) for order in orders]

    return jsonify(serialized_orders), HTTPStatus.OK
