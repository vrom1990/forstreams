pole = [
    ["0", "*", "*", "*", "*", "*", "#", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "#", "🏲", "*"],
    ["*", "*", "*", "*", "*", "*", "#", "*", "#"],
    ["*", "#", "#", "*", "*", "*", "#", "*", "*"],
    ["*", "*", "#", "*", "*", "*", "#", "#", "*"],
    ["*", "*", "#", "#", "#", "*", "#", "*", "*"],
    ["*", "*", "#", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "#", "*", "*", "*", "#", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "#", "*", "*"],
]

yi = 0
xi = 0

for ryad in pole:
    for elem in ryad:
        print(elem, end=" ")
    print()
print("Команды: влево, вправо, вниз, вверх")
command = input("Введите команду: ")

while command != "выход":
    if command == "вправо":
        if xi < 8 and pole[yi][xi + 1] != "#":
            pole[yi][xi] = "*"
            xi = xi + 1
            pole[yi][xi] = "0"
    elif command == "вниз":
        if yi < 8 and pole[yi + 1][xi] != "#":
            pole[yi][xi] = "*"
            yi = yi + 1
            pole[yi][xi] = "0"
    elif command == "влево":
        if xi > 0 and pole[yi][xi - 1] != "#":
            pole[yi][xi] = "*"
            xi = xi - 1
            pole[yi][xi] = "0"
    elif command == "вверх":
        if yi > 0 and pole[yi - 1][xi] != "#":
            pole[yi][xi] = "*"
            yi = yi - 1
            pole[yi][xi] = "0"
    else:
        print("неизвестная команда")
    for ryad in pole:
        for elem in ryad:
            print(elem, end=" ")
        print()
    if yi == 1 and xi == 7:
        print("ПОБЕДА!")
        break
    command = input("Введите команду: ")

print("Игра завершена")
