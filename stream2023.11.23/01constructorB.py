class Task():
    def __init__(self, p1, p2, p3, p4):
        self.name = p1
        self.category = p2
        self.importance = p3
        self.deadline = p3
        self.complited = False
        

task1 = Task("поспать", "отдых", "большая", "23.11.2023")
task2 = Task("поесть", "отдых", "средняя", "23.11.2023")
print(task2.name)
print(task1.complited)        