# comentario one-liner
"""
    Comentario multi
    linha
"""

# Tipos


numero_inteiro = 1
numero_decimal = 0.5
valor_logico = True
valor_logico_false = False
texto = "Exemplo Um"
texto_2 = 'Exemplo Dois'
texto_3 = """
    Um texto
    qualquer de
    multiplas linhas
"""
vazio = None

# print('Tipos:')
# soma = numero_inteiro + numero_decimal
# print(soma)

# True = 1
# soma = numero_inteiro + valor_logico
# print(soma)

# False = 0
# soma = numero_inteiro + valor_logico_false
# print(soma)

# Erro, nao é possivel somar int com str
# soma = numero_inteiro + texto
# print(soma)
# print('Ola')

# print('Type Casting:')
variavel = 5.9
# print(type(variavel))
# print(type(numero_inteiro))
# print(type(valor_logico))
# print(type(texto))
# print(int(variavel))
# print(int('Teste'))
# print(int('100'))

print('Multipla Atribuição:')
# valor1 = 1
# valor2 = 2

# valor1, valor2 = 1, 2
# valor1, valor2 = 1, 2, 3
# print(valor1)
# print(valor2)

# primeiro_valor, _, _, ultimo_valor = 10, 20, 30, 40
_, *numeros, _ = 10, 20, 30, 35, 36, 37, 40

# print(numeros)
# print(primeiro_valor)
# print(ultimo_valor)

x = False

y = 1 if x else 0

print(y)
