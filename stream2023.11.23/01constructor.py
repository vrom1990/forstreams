class Task():
    def __init__(self, name, category, importance, deadline):
        self.name = name
        self.category = category
        self.importance = importance
        self.deadline = deadline
        self.complited = False
        

task1 = Task("поспать", "отдых", "большая", "23.11.2023")
task2 = Task("поесть", "отдых", "средняя", "23.11.2023")
print(task2.name)
print(task1.complited)        