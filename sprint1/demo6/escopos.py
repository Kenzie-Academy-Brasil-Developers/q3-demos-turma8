# Escopos

x = 1
LOOP_NUMBER = 10
# FILEPATH = 'data/dados.json'


pontos = 0


def function_2():
    global pontos
    for _ in range(LOOP_NUMBER):
        pontos += 1


function_2()
print(f'{pontos=}')


def function():
    global x
    # x += 1
    x = 1000
    x += 10
    print(x)


# print(x)

# function()
