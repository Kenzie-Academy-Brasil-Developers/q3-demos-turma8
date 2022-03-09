from flask import Flask, jsonify, request
from http import HTTPStatus

# Está procurando dir services na raiz do projeto
from app.services import read_json, write_json
from app.models.car_model import Car

app = Flask(__name__)

# FILEPATH = "parking_lot.json"


@app.get("/cars")
def retrieve():
    # return jsonify(read_json(FILEPATH)), HTTPStatus.OK

    # Exemplo de pq nao utilizar método de instancia no get_cars
    # car = Car("aa", "aa", "aa", "aa", "aa")
    # return jsonify(car.get_cars()), HTTPStatus.OK

    return jsonify(Car.get_cars()), HTTPStatus.OK


@app.post("/cars")
def create():
    data = request.get_json()

    car = Car(**data)

    return car.save_car(), HTTPStatus.CREATED

    # return write_json(FILEPATH, data), HTTPStatus.CREATED
    # return , HTTPStatus.CREATED
