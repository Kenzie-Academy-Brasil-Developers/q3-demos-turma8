from time import time
from typing import Callable


def timer_measure(measure='segundos'):
    def timer(func: Callable):
        # empacotador, embrulhador
        def wrapper(*args, **kwargs):
            print('Algo acontecendo antes...')

            start = time()
            result = func(*args, **kwargs)
            end = time()

            time_elapsed = end - start

            if measure == 'segundos':
                print(f'A funcao {func.__name__} demorou {time_elapsed:.2f}s para executar')
            elif measure == 'minutos':
                print(f'A funcao {func.__name__} demorou {time_elapsed/60:.2f}m para executar')
            else:
                print(f'Argumento {measure} é invalido')

            print('Algo acontencendo depois...')

            return result
        return wrapper

    return timer
