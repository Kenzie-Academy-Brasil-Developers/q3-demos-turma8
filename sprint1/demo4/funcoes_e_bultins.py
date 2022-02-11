# Builtin zip
values = (5, 2, 3, 5)
keys = ('x', 'y', 'z')

my_dict = dict(zip(keys, values))
# print(f'{my_dict=}')


def f():
    """
        Não faz nada
    """
    ...


f()


def sum_numbers(a: int, b: int, c: float = 10.1) -> list:
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    return [a + b + c]


result = sum_numbers(1, b=5, c=1000)
print(f'{result=}')
