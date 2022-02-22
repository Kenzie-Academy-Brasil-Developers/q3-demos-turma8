from flask import Flask
# Import absoluto
# from app.decorators.decorator_with_args import timer_measure

# Import relativo
from .decorators.decorator_with_args import timer_measure


app = Flask(__name__)


MAX_RANGE = 10 ** 7
# print(__name__) == 'app'


@app.get('/')
@timer_measure('segundos')
def home():
    for _ in range(MAX_RANGE):
        ...

    return {'msg': 'olá'}
