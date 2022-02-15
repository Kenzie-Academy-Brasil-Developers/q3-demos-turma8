print('Packing e Unpacking')
# print('Args:')


def soma(a: int, b: int, c: int, d: int) -> int:
    return a + b + c + d


# sem packing
result = soma(a=1, b=2, d=3, c=4)
# print(f'{result=}')


def soma_2(word, *args):
    somatorio = 0
    print('')
    print(f'{word=}')
    print(f'{args=}')
    # args = list(args)
    for arg in args:
        somatorio += arg

    return somatorio


# result_2 = soma_2(1, 2, 3, 4, 5, 10)
# print(f'{result_2=}')

my_list = {10, 20, 30}
# result_3 = soma_2('Olá', *my_list)
# print(f'{result_3=}')


print('Kwargs:')


user = {
    'name': 'Chrystian',
    'last_name': 'Rodolfo',
    'company': 'Kenzie Academy Brasil',
    'quarter': 'Q3'
}


# Não é tao bom
def register_new_user(name: str, last_name: str, company=None):
    print('name', name)
    print('last_name', last_name)
    print('company', company)
    print('Usuario cadastrado!')


# register_new_user(user['name'], user['last_name'], user['company'])


def register_new_user_2(*args, **kwargs):
    print(f'{kwargs=}')
    for key, value in kwargs.items():
        print(f'{key} {value}')
        # break
    else:
        print('Usuario cadastrado!')

    # print('Usuario cadastrado!')


register_new_user_2(**user)
