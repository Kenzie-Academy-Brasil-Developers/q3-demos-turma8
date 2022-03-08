class Manager:
    def schedule_1_on_1(self, time: int, someone: str):
        if time < 30:
            print(f"1:1 de {time}m foi marcada com {someone}")
        else:
            print("Tempo muito longo, agende um tempo menor a 30m")

    def organize_kanban(self):
        print("Organizando Kanban...")
