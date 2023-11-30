class Person():
    def __init__(self, name, second_name, last_name, hobby, age):
        self.name = name
        self.second_name = second_name
        self.last_name = last_name
        self.hobby = hobby
        self.age = age
        self.znakomyje = []
        self.segodnya_pozdorovalis = []
        
    def znakomstvo(self, otherPerson):
        
            
        print(self.name, ": Здравствуйте, ", otherPerson.name, "!", sep="")
        print(self.name, ": Меня зовут ", self.name, sep="")
        print(self.name, ": Мне ", self.age, sep="")
        print(self.name, ": Моё увлечение — ", self.hobby, sep="")
        print()
        self.znakomyje.append(otherPerson)
        
    def privetstvie(self, otherPerson):
        if otherPerson not in self.segodnya_pozdorovalis:
            if otherPerson in self.znakomyje:
                print(self.name, ": Здравствуйте, ", otherPerson.name, "!", sep="")
                print()
            else:
                self.znakomstvo(otherPerson)
            self.segodnya_pozdorovalis.append(otherPerson)
            otherPerson.privetstvie(self)
        
Romka = Person("Роман", "Олегович", "Кизяков", "балалайка", 23)
Iiigor = Person("Игорь", "Васисуальевич", "Артамонов", "АСМР", 31)

print(Romka.segodnya_pozdorovalis)
Romka.privetstvie(Iiigor)

print(Romka.segodnya_pozdorovalis[0].name)
print(Iiigor.segodnya_pozdorovalis[0].name)


