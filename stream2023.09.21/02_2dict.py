"""
Корзина товаров
каждый товар это заголовок, картинка, цена, количество, отмечено
"""

products = [
    {"name":"батон хлеба", "img":"batooon.jpg", "price":60, "amount":2, "mark":False},
    {"name":"микроволновая печь", "img":"microvawe.jpg", "price":4000, "amount":1, "mark":True},
    {"name":"чесалка для головы", "img":"aaaaklassno.jpg", "price":700, "amount":3, "mark":True},
    {"name":"велосипед", "img":"bumbum.jpg", "price":6000, "amount":1, "mark":False},
]

command = input("Введите команду: ")
while command != "выход":
    if command == "количество":
        nomer = input("Введите номер продукта или слово «отмена»: ")
        while nomer != "отмена" and (int(nomer) < 1 or len(products) < int(nomer)):
            nomer = input("Введите номер продукта или слово «отмена»: ")
        if nomer != "отмена":
            index = int(nomer) - 1
            products[index]["amount"] = int(input("Введите новое количество: "))
    elif command == "добавить":
        product = {}
        product["name"] = input("Введите название товара: ")
        product["img"] = input("Введите название картинки: ")
        product["price"] = int(input("Введите цену: "))
        product["amount"] = 1
        product["mark"] = True
        products.append(product)
    elif command == "отметка":
        index = int(input("Введите номер продукта: "))-1
        if products[index]["mark"]:
            products[index]["mark"] = False
        else:
            products[index]["mark"] = True
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
            if product["mark"]:
                stoimost = product["price"] * product["amount"]
                itogo = itogo + stoimost
                print(
                    product["name"],
                    product["img"],
                    product["price"],
                    product["amount"],
                    stoimost,
                    product["mark"],
                    
                    sep=" | ",
                )
        print("Итого:", itogo)
        print("Подтвердить?")
        otvet = input("да/нет: ")
        if otvet == "да":
            for i in range(len(products)-1, -1, -1):
                if products[i]["mark"]:
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
            stoimost = product["price"] * product["amount"]
            itogo = itogo + stoimost
            print(
                product["name"],
                product["img"],
                product["price"],
                product["amount"],
                stoimost,
                product["mark"],
                    
                sep=" | ",
            )
        print("Итого:", itogo)
    else:
        print("Неизвестная команда")

    command = input("Введите команду: ")

print("Корзина закрыта")



