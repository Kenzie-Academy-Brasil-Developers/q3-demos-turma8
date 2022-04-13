from http import HTTPStatus

from flask import jsonify, url_for
from app.models.user_model import User
from app.services.query_service import get_by_id
from app.exc import IdNotFoundError
from dataclasses import asdict


def retrieve_by_id(user_id: int):
    try:
        user = get_by_id(User, user_id)
    except IdNotFoundError:
        return {"detail": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_user = {"orders": url_for(".retrieve_user_orders", user_id=user_id)}
    serialized_user.update(asdict(user))

    return jsonify(serialized_user), HTTPStatus.OK


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
