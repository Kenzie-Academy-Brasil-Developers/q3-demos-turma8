from app.services import read_json, write_json
import os


class Car:
    # DATABASE_FILEPATH = "parking_lot.json"
    DATABASE_FILEPATH = os.getenv("CAR_DATABASE_FILEPATH")

    def __init__(self, plate: str, company: str, model: str, color: str, spot: str):
        self.plate = plate
        self.company = company
        self.model = model
        self.color = color
        self.spot = spot

    # @staticmethod
    # def get_cars():
    # lógica de leitura do json

    # Método de instancia
    # def get_cars(self):
    #     return read_json(self.DATABASE_FILEPATH)

    @classmethod
    def get_cars(cls):
        # cls(plate='1234', company='1232')
        return read_json(cls.DATABASE_FILEPATH)

    def save_car(self):
        # objeto.__dict__
        return write_json(self.DATABASE_FILEPATH, self.__dict__)
