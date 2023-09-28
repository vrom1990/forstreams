"""
Корзина товаров
каждый товар это заголовок, картинка, цена, количество, отмечено
"""

products = [
    ["батон хлеба", "batooon.jpg", 60, 2, False],
    ["микроволновая печь", "microvawe.jpg", 4000, 1, True],
    ["чесалка для головы", "aaaaklassno.jpg", 700, 3, True],
    ["велосипед", "bumbum.jpg", 6000, 1, False],
]

command = input("Введите команду: ")
while command != "выход":
    if command == "количество":
        nomer = input("Введите номер продукта или слово «отмена»: ")
        while nomer != "отмена" and (int(nomer) < 1 or len(products) < int(nomer)):
            nomer = input("Введите номер продукта или слово «отмена»: ")
        if nomer != "отмена":
            index = int(nomer) - 1
            products[index][3] = int(input("Введите новое количество: "))
    elif command == "добавить":
        product = ['','','','','']
        product[0] = input("Введите название товара: ")
        product[1] = input("Введите название картинки: ")
        product[2] = int(input("Введите цену: "))
        product[3] = 1
        product[4] = True
        products.append(product)
    elif command == "отметка":
        index = int(input("Введите номер продукта: "))-1
        if products[index][4]:
            products[index][4] = False
        else:
            products[index][4] = True
    elif command == "оформить":
        print(
            "Название",
            "Изображение",
            "цена",
            "количество",
            "стоимость",
            "отмечено",
            sep=" | ",
        )
        itogo = 0
        for product in products:
            if product[4]:
                stoimost = product[2] * product[3]
                itogo = itogo + stoimost
                print(
                    product[0],
                    product[1],
                    product[2],
                    product[3],
                    stoimost,
                    product[4],
                    
                    sep=" | ",
                )
        print("Итого:", itogo)
        print("Подтвердить?")
        otvet = input("да/нет: ")
        if otvet == "да":
            for i in range(len(products)-1, -1, -1):
                if products[i][4]:
                    products.pop(i)
            print("Заказ оформлен, со счёта списано", itogo)
        else:
            print("Отказ от оформления заказа")
    elif command == "показать":
        print(
            "Название",
            "Изображение",
            "цена",
            "количество",
            "стоимость",
            "отмечено",
            sep=" | ",
        )
        itogo = 0
        for product in products:
            stoimost = product[2] * product[3]
            itogo = itogo + stoimost
            print(
                product[0],
                product[1],
                product[2],
                product[3],
                stoimost,
                product[4],
                
                sep=" | ",
            )
        print("Итого:", itogo)
    else:
        print("Неизвестная команда")

    command = input("Введите команду: ")

print("Корзина закрыта")


