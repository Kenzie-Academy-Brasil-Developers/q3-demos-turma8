print('\nDicionario:')
dicionario = {
    "name": 'Chrystian',
    'age': 18,
    'is_married': False
}

dicionario_2 = {(0, 1): 'valor_1', True: 'valor_2'}
dicionario_3 = {
    "name": 'Chrystian',
    "age": 18,
    "name": 'Alexandre'
}
print(f'{dicionario=}')
print(f'{dicionario_2=}')
print(f'{dicionario_3=}')

print('\nAcessando valores do Dicionario:')
print(f'{dicionario["name"]=}')
# KeyError, chave nao existe
# print(f'{dicionario["quarter"]=}')
print(f'{dicionario_2[(0, 1)]=}')

print(f'{dicionario.get("name")=}')
print(f'{dicionario.get("quarter", "A chave quarter nao existe")=}')

print('\nMétodos de Dicionario:')
# Keys
chaves = dicionario.keys()
print(chaves)
print(type(chaves))
print(list(chaves))
print(set(chaves))
print(tuple(chaves))
print('')
# Values
valores = dicionario.values()
print(valores)
print(type(valores))
print(list(valores))
print(set(valores))
print(tuple(valores))

print('\nAdicionando chave/valor Dicionario:')
# se a chave existir será substituida
dicionario['quarter'] = 'Q3-B'
print(f'{dicionario=}')
dicionario['quarter'] = 'Q3-A'
print(f'{dicionario=}')

# Adicionando múltiplos updates
print(f'{dicionario=}')
dicionario_4 = {'account_balance': 0, "children": 1}
# dicionario.update(dicionario_4)
dict_copy = dicionario.copy()
dict_copy.update(dicionario_4)
print(f'{dicionario=}')
print(f'{dict_copy=}')
