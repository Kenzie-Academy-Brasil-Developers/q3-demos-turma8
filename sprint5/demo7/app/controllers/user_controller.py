from http import HTTPStatus

from flask import jsonify
from app.models.user_model import User


def retrieve_by_id(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return {"error": "user id not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user), HTTPStatus.OK


def retrieve_user_orders(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return {"error": "user id not found"}, HTTPStatus.NOT_FOUND

    return jsonify(user.orders), HTTPStatus.OK


def retrieve_user_invoices(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return {"error": "user id not found"}, HTTPStatus.NOT_FOUND

    return jsonify([order.invoice for order in user.orders]), HTTPStatus.OK
