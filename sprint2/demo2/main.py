from decorators.decorator_comum import timer
from decorators.decorator_with_args import timer_measure

MAX_RANGE = 10 ** 8


def common_function(max_range: int):
    for _ in range(max_range):
        ...

# decorator do flask
# @app.route('/')

# @timer
# def common_function(max_range: int):
#     for _ in range(max_range):
#         ...


# @timer_measure('minutos')
# def common_function(max_range: int):
#     for _ in range(max_range):
#         ...


common_function(MAX_RANGE)
