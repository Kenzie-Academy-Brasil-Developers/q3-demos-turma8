from flask_httpauth import HTTPTokenAuth
from app.models.user_model import User
import os

auth = HTTPTokenAuth()
# auth = HTTPTokenAuth(scheme='Bearer')


# @auth.verify_token
# def verify_token(api_key: str):
#     user = User.query.filter_by(api_key=api_key).first()

#     return user


"""
    Supondo ser um serviço interno, não teria por que ter uma API_KEY para cada user,
    poderia ter uma API_KEY geral para o sistema, que ficaria no .env
"""


@auth.verify_token
def verify_token(api_key: str):
    return api_key == os.getenv('API_KEY')
