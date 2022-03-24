from http import HTTPStatus
from flask import jsonify, request
from app.models.user_model import User
from psycopg2.errors import UniqueViolation


def get_users():
    users = User.read_users()
    print(users)

    user_columns = [
        "_id",
        "email",
        "birthdate",
        "children",
        "married",
        "account_balance",
    ]

    serialized_users = [dict(zip(user_columns, user)) for user in users]

    return jsonify(serialized_users)


def get_user_by_id(user_id):
    return {"msg": "Rota de busca de usuario por id"}


def add_user():
    data = request.get_json()

    user = User(**data)
    try:
        inserted_user = user.create_user()
    except UniqueViolation as e:
        # return {"error": e.args}, HTTPStatus.UNPROCESSABLE_ENTITY
        return {"error": "email already in use"}, HTTPStatus.UNPROCESSABLE_ENTITY

    user_columns = [
        "_id",
        "email",
        "birthdate",
        "children",
        "married",
        "account_balance",
    ]

    serialized_user = dict(zip(user_columns, inserted_user))

    return serialized_user, HTTPStatus.CREATED
