from app.exceptions import InvalidPlateError

from .json_handler import read_json


def car_already_parked(filepath: str, plate: str):
    cars_list = read_json(filepath)

    # for car in cars_list:
    #     if car["plate"] == plate:
    #         return True

    # return False
    return [car["spot"] for car in cars_list if car["plate"] == plate]


def spot_already_taken(filepath: str, spot: str):
    cars_list = read_json(filepath)

    # Equivale a verificação car_already_parked
    return [car for car in cars_list if car["spot"] == spot]


def validate_plate(plate: str):
    # AAA-1333
    if (
        plate[:3].isalpha()
        and plate[4:].isnumeric()
        and len(plate) == 8
        and plate[3] == "-"
    ):
        return plate.upper()

    raise InvalidPlateError
