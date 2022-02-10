print('\nTuplas:')
"""
    Tuplas nao podem ter
    seus valores reatribuidos
"""
tupla = (1, 2, 3, 3)
tupla_2 = (3.9, ['Chrystian', 100], '2')

print(f'{tupla=}')
print(f'{tupla_2=}')

print('\nAcessando itens de Tuplas:')
print(f'{tupla[0]=}')
print(f'{tupla_2[1]=}')
print(f'{tupla_2[1][0]=}')

print('\nMétodos de Tuplas:')
print(f'{tupla.count(3)=}')
print(f'{tupla.count(1)=}')

print(f'{tupla.index(3)=}')
print(f'{tupla.index(1)=}')

print('\nReatribuindo valores de Tuplas:')
# tupla[0] = 100

# Lista é mutável, portanto pode ser alterada dentro
# de uma tupla
tupla_2[1][0] = 'Marcelo'
print(f'{tupla_2=}')
