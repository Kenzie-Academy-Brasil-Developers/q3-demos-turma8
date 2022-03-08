from demo2_classes import Teacher, Enabler, Manager, Instructor

# 1 -
# t1 = Teacher("Teacher 1", "2222222")
# print(f"{t1=}")
# print(f"{t1.__dict__=}")
# t1.enter_meeting("3821637812637962178")
# t1.batatinha = "batatinha"
# print(f"{t1.__dict__=}")

# 2 -
# e1 = Enabler("Enabler 1", "q3", ["Coach1", "Coach2"])
# print(f"{e1=}")
# print(f"{e1.__dict__=}")
# print(f"{e1.quarters=}")
# e1.schedule_1_on_1(60, "Alguem")
# e1.schedule_1_on_1(60, "Coach1")

# 3 -
# m1 = Manager()
# m1.schedule_1_on_1(30, "OutroAlguem")
# m1.schedule_1_on_1(29, "OutroAlguem2")
# m1.organize_kanban()

# 4 -
# i1 = Instructor("Instructor 1", "Q2")
# print(f"{i1=}")
# print(f"{i1.__dict__=}")

# i1.start_demo()
# i1.start_demo()
# i1.end_demo()
# i1.end_demo()

# i1.schedule_1_on_1(60, "MaisOutroAlguem")

# i1.start_demo()
# i1.organize_kanban()
# i1.end_demo()
# i1.organize_kanban()

# 5 -
t1 = Teacher("Teacher 1", "2222222")
t1.schedule_1_on_1(30, "Fulano")

e1 = Enabler("Enabler 1", "q3", ["Coach1", "Coach2"])
e1.schedule_1_on_1(20, "Coach1")

i1 = Instructor("Instructor 1", "Q2")
i1.schedule_1_on_1(60, "MaisOutroAlguem")
