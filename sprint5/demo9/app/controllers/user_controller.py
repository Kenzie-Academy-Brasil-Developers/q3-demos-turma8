from http import HTTPStatus

from flask import jsonify, request, url_for
from app.models.user_model import User
from app.services.query_service import get_by_id
from app.exc import IdNotFoundError, InvalidEmailError, InvalidDateFormatError
from dataclasses import asdict
from app.configs.database import db
import sqlalchemy
import psycopg2


def create_user():
    data = request.get_json()

    try:
        user = User(**data)
    except InvalidEmailError:
        return {"detail": "email must contain `churros`"}, HTTPStatus.BAD_REQUEST
    except InvalidDateFormatError:
        return {"detail": "date format must be `yyyy/mm/dd`"}, HTTPStatus.BAD_REQUEST

    try:
        db.session.add(user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        # if type(e.orig) == psycopg2.errors.UniqueViolation:
        #     return {"error": "Unique Violation"}, HTTPStatus.UNPROCESSABLE_ENTITY
        # if type(e.orig).__name__ == "UniqueViolation":
        #     return {"error": "Unique Violation"}, HTTPStatus.UNPROCESSABLE_ENTITY
        if isinstance(e.orig, psycopg2.errors.UniqueViolation):
            return {"error": "Unique Violation"}, HTTPStatus.UNPROCESSABLE_ENTITY

        return {"error": "Integrity Error"}, HTTPStatus.UNPROCESSABLE_ENTITY

    return jsonify(user), HTTPStatus.OK


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
