from http import HTTPStatus
from flask import Flask, request


app = Flask(__name__)


@app.get("/dict")
def dict_view():
    return {"key": "value"}, HTTPStatus.OK


@app.post("/sort-list")
def sort_list():
    body = request.get_json()

    if type(body["data"]) is not list:
        return {"error": 'o body deve conter o formato {"data": <lista>}'}, 400

    body["data"].sort()

    return body, HTTPStatus.OK
