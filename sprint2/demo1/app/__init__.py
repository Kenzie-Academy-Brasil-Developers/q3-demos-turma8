from flask import Flask, jsonify
from http import HTTPStatus
import os

from app.pacote_a.modulo_a_1 import my_function

app = Flask(__name__)


# Forma antiga
# @app.route('/', methods=["GET"])
# def home():
#     return 'Olá'

@app.get('/')
def home():
    return {'msg': 'Bom dia Q3'}


@app.get('/primeira_rota')
def primeira_rota():
    variavel = os.getenv("MINHA_VARIAVEL")
    variavel_nao_exitente = os.getenv("ALGUMA_COISA")

    return {'msg': f'{variavel}', "msg2": f'{variavel_nao_exitente}'}

@app.get('/segunda_rota')
def segunda_rota():

    return jsonify([number for number in range(10)]), HTTPStatus.UNAUTHORIZED

@app.get('/terceira_rota')
def terceira_rota():

    return jsonify(my_function()), HTTPStatus.OK

    """
    Propriedades JSON
        Sempre a chave é uma string
        Strings são representadas por aspas duplas
    """