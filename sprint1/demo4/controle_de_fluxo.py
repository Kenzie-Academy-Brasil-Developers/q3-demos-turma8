# import datetime
from datetime import datetime
import time

# print('\nWhile:')

# { } nao preciso de chaves para blocos
# while(True):
#     time.sleep(1)
#     print(datetime.now().time())
#     second = datetime.now().second

#     if second % 2 == 0:
#         print('pulei')
#         # pula para o proximo laço da iteração
#         # continue

#     print('Pós IF')
#     if second == 50:
#         break


# print('\nFor:')
# lista = [10, 20, 30]
# print(f'{lista=}')

# for(let i=0; i<lista.length; i++)
# for i in range(len(lista)):
#     print(lista[i])

# for item in lista:
#     print(item)

# print('')

# chrystian = ['linux']
# gustavo = ['linux', 'windows']

# # Lista de listas
# usuarios = [chrystian, gustavo]

# for usuario in usuarios:
#     print(usuario)
#     for so in usuario:
#         print(so)

# for index, item in enumerate(lista, 250):
#     print(index)
#     # print(item)


# for numero in range(10, 20, 2):
#     print(numero)

# print('\nFor em dicionario')
# my_dict = {'name': 'Chrystian', "quarter": 'Q3'}
# print(f'{my_dict=}')
# print('')
# for x in my_dict:
#     print(x)

# for key in my_dict.keys():
#     print(key)

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     # print(key)
#     print(value)


print('\nOperadores lógicos:')
result = None
log = True

# if result or log:
#     print('result ou log sao "trutys"')
# else:
#     print('result e log sao "falsys"')

# if result and log:
#     print('result e log sao "trutys"')
# else:
#     print('result ou log sao "falsys"')


# number = 5
number = 8
# number = 11

# Pythonica
is_valid = 1 < number < 10 and number != 8 and number % 2 != 0

if is_valid:
    print('Numero válido')
elif result:
    print('Result foi true, numero valido')
else:
    print('Else')
