print('Listas:')
lista = [1, 2, 3]
lista_2 = ['Chrystian', 2, 3.5, True]
print(type(lista))

print('\nAcessando e modificando elementos:')
print('estado atual de lista = ', lista)
# print(lista[0])
# print(lista[:2])
# print(lista[::-1])
# print(lista)
lista[0] = 7
print(lista)

print('\nTamanho de lista:')
print('estado atual de lista = ', lista)
print('Tamanho', len(lista))

print('\nOrdenação:')
# print('estado atual de lista = ', lista)
# print(lista.sort())
# print(lista)
# # Descendente
# print(lista.sort(reverse=True))
# print(lista)
# Nao quero alterar o objeto em si
lista_sorted = sorted(lista)
print(f'{lista_sorted}')
print(f'{lista}')

lista_sorted = sorted(lista, reverse=True)
print(f'{lista_sorted}')
print(f'{lista}')


print('\nInserindo itens:')
print('estado atual de lista = ', lista)
lista.append(100)
lista.append(100)
print(f'{lista=}')

print('\nDeletando itens:')
print('estado atual de lista = ', lista)
# lista.remove(100)
# print(f'{lista=}')
# pop
elemento_removido = lista.pop(0)
print(f'{lista=}')
print(f'{elemento_removido=}')

elemento_removido = lista.pop(1000)
print(f'{lista=}')
print(f'{elemento_removido=}')
