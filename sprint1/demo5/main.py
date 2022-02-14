import math


def delta(a: int, b: int, c: int) -> float:
    """Calcula o delta de 3 numeros

    Args:
        a (int): numero inteiro
        b (int): numero inteiro
        c (int): inteiro

    Returns:
        float: Retorna o resultado de delta
    """
    # b^2 - 4ac
    # b ** 2
    # b * b
    return pow(b, 2) - 4 * a * c


# Firacode -> === !=
def bhaskara(a: int, b: int, c: int) -> tuple[float]:
    d = delta(a, b, c)

    print(f'{d=}')

    if d < 0:
        return 'Delta negativo'

    # raiz_quadrada = math.sqrt(d)
    raiz_delta = round(math.sqrt(d), 2)
    print(f'{raiz_delta=}')

    x1 = round((-b + raiz_delta) / 2 * a, 2)
    x2 = round((-b - raiz_delta) / 2 * a, 2)

    # print(f'{x1=}')
    # print(f'{x2=}')

    return x1, x2


res1, res2 = bhaskara(1, 5, 2)

print(f'{res1=}')
print(f'{res2=}')
