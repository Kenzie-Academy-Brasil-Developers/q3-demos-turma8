from http import HTTPStatus
from flask import jsonify, request
from app.models.user_model import User
from psycopg2.errors import UniqueViolation


def get_users():
    email = request.args.get("email")

    if email:
        users = User.read_users_by_email(email)
        serialized_users = [User.serialize(user) for user in users]

        return jsonify(serialized_users)

    users = User.select_all()
    print(f"{users=}")

    return jsonify(users)
    # return jsonify(serialized_users)


def get_user_by_id(user_id):
    return {"msg": "Rota de busca de usuario por id"}


def add_user():
    data = request.get_json()

    user = User(**data)
    try:
        # inserted_user = user.create_user()
        inserted_user = user.insert_into()
    except UniqueViolation as e:
        # return {"error": e.args}, HTTPStatus.UNPROCESSABLE_ENTITY
        return {"error": "email already in use"}, HTTPStatus.UNPROCESSABLE_ENTITY

    serialized_user = User.serialize(inserted_user)

    return serialized_user, HTTPStatus.CREATED


def update_user(user_id: str):
    data = request.get_json()

    updated_user = User.update_user(user_id, data)

    if not updated_user:
        return {"error": "id not found"}, HTTPStatus.NOT_FOUND

    serialized_user = User.serialize(updated_user)

    return serialized_user, HTTPStatus.OK
