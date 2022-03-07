from datetime import datetime as dt


class Person:
    # Atributos de Classe
    # int -> Imutável
    life_expectancy = 90
    # list -> Mutáveis
    shopping_list = ["Violão"]

    # Método inicializador
    # Método de instancia
    def __init__(self, name: str, cpf: str, pet: bool = False):
        # Atributos de Instancia
        self.name = name
        self.cpf = cpf
        self.pet = pet
        self.created_at = dt.now().strftime("%d/%m/%Y %H:%M:%S")
        self.partner = None
        self.steps = 0
        self.tasks = []

    def __repr__(self) -> str:
        return f"<{self.name} - {self.cpf}>"

    @staticmethod
    def marry(person1: "Person", person2: "Person"):
        # person1.partner = person2
        # person2.partner = person1

        person1.partner, person2.partner = person2, person1

    # Método de instancia
    def walk(self, steps_walked: int = 1):
        self.steps += steps_walked
