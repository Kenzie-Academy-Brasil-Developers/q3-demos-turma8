# List Comprehension
MAX_RANGE = 7

lista_1 = []

for i in range(MAX_RANGE):
    if i % 2 == 0:
        lista_1.append('Par')
    else:
        lista_1.append('Impar')

# 'Faça 1' se True else 'Faça 2'

# PEP-8
lista_2 = [i for i in range(MAX_RANGE) if i % 2]
lista_3 = [
    'Par' if i % 2 == 0 else 'Impar'
    for i in range(MAX_RANGE)
]
lista_4 = [i * 50 for i in range(MAX_RANGE) if i % 2 == 0]

vogais = 'aeiou'
"""
Equivalente
for index, letra in enumerate(vogais):
     print(letra * index)
"""
lista_5 = [index * vogal for index, vogal in enumerate(vogais)]

print(f'{lista_1=}')
print(f'{lista_2=}')
print(f'{lista_3=}')
print(f'{lista_4=}')
print(f'{lista_5=}')
