spisok = ["масло", "хлеб", "огурцы"]

print("СПИСОК ПОКУПОК")
for elem in spisok:
    print("-", elem)

command = input("Введите команду: ")
while command != "выход":
    if command == "добавить":
        newProduct = input("Введите новый товар: ")
        spisok.append(newProduct)
    elif command == "удалить":
        delProduct = input("Какой товар удалить?: ")
        if delProduct in spisok:
            spisok.remove(delProduct)
        else:
            print("Такого товара нет! ")
    elif command == "отредактировать":
        product = input("Какой товар отредактировать?: ")
        if product in spisok:
            i = spisok.index(product)
            print("Редактируется товар", spisok[i])
            spisok[i] = input("Введите новое название товара: ")
        else:
            print("Такого товара в списке нет.")
    else:
        print("Неизвестная команда")
    print("СПИСОК ПОКУПОК")
    for elem in spisok:
        print("-", elem)
    command = input("Введите команду: ")
    
print("Программа закрыта")