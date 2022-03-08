class Teacher:
    quarters = ("Q1", "Q2", "Q3", "Q4")
    # lista

    def __init__(self, name: str, quarter: str):
        self.name = name
        self.quarter = quarter.upper() if quarter.upper() in self.quarters else "Q1"
        self.is_in_meeting = False

    def enter_meeting(self, meeting_id: str):
        self.is_in_meeting = True
        self.meeting_id = meeting_id

    def schedule_1_on_1(self, time: int, someone: str):
        # print(f"1:1 de {time}m foi marcada com {someone} por {self.name}")
        print(f"1:1 de {time}m foi marcada com {someone} por {self.__repr__()}")

    def __repr__(self):
        return f"<{self.name}:{self.quarter}>"
