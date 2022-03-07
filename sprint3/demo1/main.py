from demo_classes import Person

# 1 - atributos_1
# p1 = new Person()
# p1 = Person()
# p2 = Person()
# p3 = Person()

# print(f"{p1=}")
# print(f"{p2=}")
# print(f"{p3=}")

# p1.life_expectancy = 30
# print(f"{p1.life_expectancy=}")
# print(f"{p2.life_expectancy=}")
# print(f"{p3.life_expectancy=}")

# p1.shopping_list.append("Teclado")
# print(f"{p1.shopping_list=}")
# print(f"{p2.shopping_list=}")
# print(f"{p3.shopping_list=}")

# 2 - inicializador
# p1 = Person("person1", "1111")
# p2 = Person("person2", "2222")
# p3 = Person("person3", "3333")

# # p1.name = "Outro nome1"
# print(f"{p1.name=}")
# print(f"{p2.name=}")
# print(f"{p3.name=}")

# print(f"{p1.__dict__=}")

# print(f"{p1=}")
# print(f"{p2=}")
# print(f"{p3=}")

# 3 - atributos_2
# p1 = Person("person1", "1111", True)
# p2 = Person("person2", "2222")
# p3 = Person("person3", "3333")

# print(f"{p1.__dict__=}")
# print(f"{p2.__dict__=}")
# print(f"{p3.__dict__=}")

# 4 - metodo_estatico
# p1 = Person("person1", "1111", True)
# p2 = Person("person2", "2222")

# # Utilizando staticmethod
# # Person.marry(p1, p2)

# p3 = Person("person3", "3333")

# p3.marry(p1, p2)

# print(f"{p1.__dict__=}")
# print(f"{p2.__dict__=}")

# 5 - metodo_de_instancia
p1 = Person("person1", "1111", True)
p2 = Person("person2", "2222")

p1.walk()
p2.walk(50)

p1.tasks.append("Task Person 1")
p2.tasks.append("Task Person 2")

print(f"{p1.__dict__=}")
print(f"{p2.__dict__=}")

p1.shopping_list.append("Bateria")

print(f"{p1.tasks=}")
print(f"{p1.shopping_list=}")

print(f"{p2.tasks=}")
print(f"{p2.shopping_list=}")

# Person.walk(10)
Person.walk(p1, 10)
print(f"{p1.__dict__=}")
