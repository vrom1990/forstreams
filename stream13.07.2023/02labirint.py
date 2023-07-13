from random import randint

pole = [
    ["0", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "🏲"],
]

yi = 0
xi = 0


wallCount = int(input("Введите количество стенок: "))

while wallCount > 30:
    print("Слишком много!")
    wallCount = int(input("Введите количество стенок: "))

for step in range(wallCount):
    wy = randint(0, 8)
    wx = randint(0, 8)
    while pole[wy][wx] == "#" or pole[wy][wx] == "0" or pole[wy][wx] == "🏲":
        wy = randint(0, 8)
        wx = randint(0, 8)
    pole[wy][wx] = "#"


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
