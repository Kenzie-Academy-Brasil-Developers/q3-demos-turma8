from http import HTTPStatus

from flask import Flask, jsonify, request

from app.exceptions import (
    CarAlreadyParkedError,
    InvalidPlateError,
    SpotAlreadyTakenError,
)
from app.models.car_model import Car


app = Flask(__name__)


@app.get("/cars")
def retrieve():

    return jsonify(Car.get_cars()), HTTPStatus.OK


@app.post("/cars")
def create():
    data = request.get_json()

    try:
        car = Car(**data)
        return car.add_car(), HTTPStatus.CREATED
    except InvalidPlateError as e:
        return {"error": e.message}, e.status_code
    except CarAlreadyParkedError as e:
        # return {"error": f"Plate {car.plate} already parked"}, HTTPStatus.CONFLICT
        return {"error": e.message}, e.status_code
    except SpotAlreadyTakenError as e:
        # return {"error": f"Spot {car.spot} already taken"}, HTTPStatus.CONFLICT
        return {"error": e.message}, e.status_code
