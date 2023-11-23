class Person():
    pass

serega = Person()
serega.name = input("Введите имя: ")
serega.last_name = input("Введите фамилию: ")
serega.age = input("Введите возраст: ")

print("Здравствуйте, дорогой", serega.name, serega.last_name)

person2 = Person()
person2.name = input("Введите имя: ")
person2.last_name = input("Введите фамилию: ")
person2.age = input("Введите возраст: ")

print("Здравствуйте, дорогой", person2.name, serega.last_name)