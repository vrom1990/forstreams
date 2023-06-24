pole = ["*", "*", "*", "*", "0", "*", "*", "*", "*", "*"]
i = 4

for elem in pole:
    print(elem, end="")
print()
command =  input("Введите команду: ")   
while command != "выход":
    if command == "стоять":
        pass
    elif command == "вправо":
        if i < 9:
            pole[i] = "*"
            i = i + 1
            pole[i] = "0"
            
    elif command == "влево":
        if i > 0:
            pole[i] = "*"
            i = i - 1
            pole[i] = "0"
            
    else:
        print("Неизвестная команда")
    for elem in pole:
        print(elem, end="")
    print()
    command =  input("Введите команду: ")
    
print("Программа завершена")
