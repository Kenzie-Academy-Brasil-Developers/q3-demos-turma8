print('Mutabilidade e imutabilidade\n')


def random_function(param1: list):
    param1.append(10000)


# my_list = [1, 2, 3]
# print(f'{my_list=}')
# random_function(my_list)
# print(f'{my_list=}')


def random_function_2(*param1: list):
    param1 = list(param1)
    param1.append(10000)


# my_list = [1, 2, 3]
# print(f'{my_list=}')
# random_function_2(*my_list)
# print(f'{my_list=}')


# desempacotamento cria uma cópia do dicionario
def random_function_3(**param1: dict):
    param1['quarter'] = 'M5'


# user = {'name': 'Chrystian', 'quarter': 'Q3'}
# print(f'{user=}')
# random_function_3(**user)
# print(f'{user=}')


def random_function_3(param1: dict):
    param1['quarter'] = 'M5'


user = {'name': 'Chrystian', 'quarter': 'Q3'}
print(f'{user=}')
random_function_3(user)
print(f'{user=}')
