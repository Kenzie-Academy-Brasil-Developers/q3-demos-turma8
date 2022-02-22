from time import time
from typing import Callable


def timer(func: Callable):
    # empacotador, embrulhador
    def wrapper(*args, **kwargs):
        print('Algo acontecendo antes...')

        start = time()
        result = func(*args, **kwargs)
        end = time()

        time_elapsed = end - start
        print(f'A funcao {func.__name__} demorou {time_elapsed:.2f}s para executar')

        print('Algo acontencendo depois...')

        return result
    return wrapper
