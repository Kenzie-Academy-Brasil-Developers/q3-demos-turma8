from time import time
from typing import Callable


def timer_measure(measure='segundos'):
    def timer(func: Callable):
        # empacotador, embrulhador
        def wrapper(*args, **kwargs):
            print('Algo acontecendo antes...')

            start = time()
            result: dict = func(*args, **kwargs)
            end = time()

            time_elapsed = end - start

            if measure == 'segundos':
                print(f'A funcao {func.__name__} demorou {time_elapsed:.2f}s para executar')
            elif measure == 'minutos':
                print(f'A funcao {func.__name__} demorou {time_elapsed/60:.2f}m para executar')
            else:
                print(f'Argumento {measure} é invalido')

            print('Algo acontencendo depois...')

            # print(f'{result=}')
            time_elapsed_formated = f'{time_elapsed:.2f}s'
            result.update({'time_elapsed': time_elapsed_formated})

            return result
        return wrapper

    return timer
