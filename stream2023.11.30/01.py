class Person():
    def __init__(self, name, second_name, last_name, hobby, age):
        self.name = name
        self.second_name = second_name
        self.last_name = last_name
        self.hobby = hobby
        self.age = age
        
    def znakomstvo(self):
        print("Здравствуйте!")
        print("Меня зовут", self.name)
        print("Мне", self.age)
        print("Моё увлечение —", self.hobby)
        
    def privetstvie(self, znakom, name):
        if znakom:
            print("Здравствуйте, ", name, "!", sep="")
        else:
            self.znakomstvo()
        
Romka = Person("Роман", "Олегович", "Кизяков", "балалайка", 23)
Iiigor = Person("Игорь", "Васисуальевич", "Артамонов", "АСМР", 31)

Romka.privetstvie(False, "Сергей")