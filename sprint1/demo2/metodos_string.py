print('Métodos de string:')
nome_completo = 'Chrystian Rodolfo'
print(nome_completo[1])
# Interpolação
# length, lenght, legnht
print(f'Tamanho {len(nome_completo)}')
print(f'nome_completo={nome_completo}')
print(f'{nome_completo=}')

lista_nome = nome_completo.split()
lista_letra_nome = list(nome_completo)
print(f'{lista_nome=}')
# print(f'{lista_letra_nome=}')

# nome, sobrenome = nome_completo.split()
nome, sobrenome = lista_nome
print(f'{nome=}')
print(f'{sobrenome=}')

lista_2 = ['Alexandre', 'Alves']
nome_completo_join = " ".join(lista_2)
print(f'{nome_completo_join=}')

print('\nSlicing de string:')
print(f'{nome_completo_join=}')
print(nome_completo_join[0])
# [0, 2[
print(nome_completo_join[0:2])
print(nome_completo_join[:5])
print(nome_completo_join[2:])
print(nome_completo_join[len(nome_completo_join) - 1])
print(nome_completo_join[-1])
print(nome_completo_join[-2])
print(nome_completo_join[:-2])
print(nome_completo_join[::2])
print(nome_completo_join[::-1])



