import os

from app.exceptions import CarAlreadyParkedError, SpotAlreadyTakenError
from app.services import read_json, write_json
# from app.services.car_service import (
#     car_already_parked,
#     spot_already_taken,
#     validate_plate,
# )
from app.services.car_service import (car_already_parked, spot_already_taken,
                                      validate_plate)


class Car:
    # DATABASE_FILEPATH = "parking_lot.json"
    DATABASE_FILEPATH = os.getenv("CAR_DATABASE_FILEPATH")

    def __init__(self, plate: str, company: str, model: str, color: str, spot: str):
        self.plate = validate_plate(plate)
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot

    @classmethod
    def get_cars(cls):
        return read_json(cls.DATABASE_FILEPATH)

    def add_car(self):
        # objeto.__dict__
        # car = self.__dict__

        parked = car_already_parked(self.DATABASE_FILEPATH, self.plate)

        if parked:
            spot_parked = parked[0]
            # raise CarAlreadyParkedError(
            #     message="MENSAGEM ALEATORIA", spot=spot_parked, plate=self.plate
            # )
            raise CarAlreadyParkedError(spot=spot_parked, plate=self.plate)

        if spot_already_taken(self.DATABASE_FILEPATH, self.spot):
            # raise SpotAlreadyTakenError(message="mensagem!!!!")
            raise SpotAlreadyTakenError(spot=self.spot)

        return write_json(self.DATABASE_FILEPATH, self.__dict__)
