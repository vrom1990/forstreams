"""
Корзина товаров
каждый товар это заголовок, картинка, цена, количество, отмечено
"""

product = {"name":"батон хлеба", "img":"batooon.jpg", "price":60, "amount":2, "mark":False}


command = input("Введите команду: ")
while command != "выход":
    if command == "количество":
        product["amount"] = int(input("Введите новое количество: "))
    elif command == "отметка":
        if product["mark"]:
            product["mark"] = False
        else:
            product["mark"] = True
    
    elif command == "показать":
        stoimost = product["price"]*product["amount"]
        print(
            "Название",
            "Изображение",
            "цена",
            "количество",
            "стоимость",
            "отмечено",
            sep=" | ",
        )
        print(
                product["name"],
                product["img"],
                product["price"],
                product["amount"],
                stoimost,
                product["mark"],
                
                sep=" | ",
        )
    else:
        print("Неизвестная команда")

    command = input("Введите команду: ")

print("Корзина закрыта")



