import secrets
from datetime import timedelta

from flask import jsonify, request
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)

from app.configs.auth import auth
from app.configs.database import db
from app.models.user_model import User


@jwt_required()
def profile():
    user = get_jwt_identity()

    # buscar produtos relacionados ao usuario
    return jsonify(user)


@jwt_required()
def list_users():
    users = User.query.all()

    return jsonify(users), 200


# @auth.login_required
def login_user():
    data = request.get_json()

    user: User = User.query.filter_by(email=data['email']).first()

    if not user or not user.check_password(data['password']):
        return {'detail': 'email and password missmatch'}, 401

    # poderia montar dicionario antes, e associar só o que eu quero a identity
    token = create_access_token(user, expires_delta=timedelta(minutes=1))

    return jsonify({'token': token}), 200


def create_user():
    data = request.get_json()

    data['api_key'] = secrets.token_urlsafe(32)

    user: User = User(**data)

    db.session.add(user)
    db.session.commit()

    return jsonify(user), 200
