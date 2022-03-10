# class CarAlreadyParkedError(Exception):
#     ...


# class SpotAlreadyTakenError(Exception):
#     ...


class CarAlreadyParkedError(Exception):
    def __init__(
        self, message=None, status_code=409, spot="not informed", plate="not informed"
    ):

        if not message:
            self.message = f"Plate {plate} already parked in {spot}"
        else:
            self.message = message

        self.status_code = status_code


class SpotAlreadyTakenError(Exception):
    def __init__(self, message=None, status_code=409, spot="not informed"):

        if not message:
            self.message = f"Spot {spot} already taken!!"
        else:
            self.message = message

        self.status_code = status_code


class InvalidPlateError(Exception):
    def __init__(self, message=None, status_code=400):

        if not message:
            self.message = f"Plate must be in format AAA-1111"
        else:
            self.message = message

        self.status_code = status_code
