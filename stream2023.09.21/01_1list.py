"""
Корзина товаров
каждый товар это заголовок, картинка, цена, количество, отмечено
"""

product = ["батон хлеба", "batooon.jpg", 60, 2, False]


command = input("Введите команду: ")
while command != "выход":
    if command == "количество":
        product[3] = int(input("Введите новое количество: "))
    elif command == "отметка":
        if product[4]:
            product[4] = False
        else:
            product[4] = True
    
    elif command == "показать":
        stoimost = product[2]*product[3]
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
                product[0],
                product[1],
                product[2],
                product[3],
                stoimost,
                product[4],
                
                sep=" | ",
        )
    else:
        print("Неизвестная команда")

    command = input("Введите команду: ")

print("Корзина закрыта")


