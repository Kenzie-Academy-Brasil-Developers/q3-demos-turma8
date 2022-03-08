from demo2_classes import Teacher, Manager


class Instructor(Teacher, Manager):
    # DOCTSTRING
    """
    Classe Insctructor que herda de Teacher e Manager
    """

    def __init__(self, name: str, quarter: str):
        # Manager.__init__(name, quarter)
        super().__init__(name, quarter)
        self.is_in_demo = False

    def start_demo(self):
        if not self.is_in_demo:
            print("Demo iniciada...")
            self.is_in_demo = True
        else:
            print("Já esta em uma demo.")

    def end_demo(self):
        if self.is_in_demo:
            print("Demo encerrada.")
            self.is_in_demo = False
        else:
            print("Você não está em uma demo")

    def organize_kanban(self):
        # Manager.organize_kanban()
        # Teacher.organize_kanban()
        if not self.is_in_demo:
            super().organize_kanban()
        else:
            print("Ocupado")
