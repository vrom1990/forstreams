persons = [{"name": "Микордий","surname": "Сердюков","pol": "м"},
           {"name":"Иванна" ,"surname": "Ниточкина","pol": "ж"},
           {"name": "Практикантий" ,"surname": "Круглоходов","pol": "м"}]

def hello(name, surname, pol):
    if pol == "м":
        print(name, surname + ", господин, здравствуйте!")
        print("Очень рады видеть столь серьёзного человека среди нас!")
        print("Приходите, гардероб на первом этаже слева,")
        print("Туалет на втором этаже тоже слева")
    else:
        print(name, surname + ", госпожа, здравствуйте!")
        print("Очень рады видеть столь прекрасную даму в нашем обществе!")
        print("Приходите, гардероб на первом этаже справа,")
        print("Туалет на втором этаже тоже справа")
    print("До скорой встречи!")
    print()
    
for person in persons:
    hello(person["name"], person["surname"], person["pol"])
    
name = input("Здравствуйте! Как вас зовут?: ")
while name != "стоп":
    surname = input("Напомните вашу фамилию, пожалуйста!: ")
    pol = input("Ввод пола: ")
    hello(name, surname, pol)
    name = input("Здравствуйте! Как вас зовут?: ")
