from demo2_classes import Teacher


# equivalente ao extends do JS
class Enabler(Teacher):
    def __init__(self, name: str, quarter: str, coaches: list[str]):
        super().__init__(name, quarter)
        self.coaches = coaches

    def schedule_1_on_1(self, time: int, someone: str):
        if someone in self.coaches:
            return super().schedule_1_on_1(time, someone)

        print(f"{someone} não está na minha lista de coaches, 1:1 não agendada")
