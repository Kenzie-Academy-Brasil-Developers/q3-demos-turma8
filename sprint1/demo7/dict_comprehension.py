# Dict Comprehension

ford = {
    'brand': "Ford",
    "eletric": False,
    "year": 1979,
    "colors": ['red', 'white', 'gray']
}

fiat = {
    'brand': "Fiat",
    "eletric": False,
    "year": 2021,
    "colors": ['blue', 'white']
}

bmw = {
    'brand': "BMW",
    "eletric": False,
    "year": 1993,
    "colors": ['black']
}

ferrari = {
    'brand': "Ferrari",
    "eletric": True,
    "year": 2021,
    "colors": ['black', 'blue', 'white', 'red']
}

dict_1 = {key: value for key, value in ford.items()}
# dict_2 = {item for item in ford.keys()}
dict_3 = {key: value for key, value in ford.items() if key != 'colors'}
dict_4 = {key: value if type(value) is int else 'not int' for key, value in ford.items()}

print(f'{dict_1=}')
print(f'{dict_3=}')
print(f'{dict_4=}')
# print(f'{dict_2=}')
# print(f'{type(dict_2)=}')
