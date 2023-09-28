def calc():
    command = input("Введите команду калькулятора: ")
    while command != "выход":
        if command == "+":
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите второе число: "))
            print("Сумма:", num1+num2)
        elif command == "-":
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите второе число: "))
            print("Разность:", num1-num2)
        elif command == "*":
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите второе число: "))
            print("Произведение:", num1*num2)
        elif command == "/":
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите второе число: "))
            print("Частное:", num1/num2)
        else:
            print("Неизвестная команда!")
        command = command = input("Введите команду калькулятора: ")

def anekdot():
    print("Шла как-то машина по медведю, видит: лес горит.")
    print("Села в него и сгорела.")
    
def sovet():
    print("Тарелку после гречки мой сразу.")
    
command = input("Введите команду: ")
while command != "выход":
    if command == "анекдот":
        anekdot()
    elif command == "совет":
        sovet()
    elif command == "калькулятор":
        calc()
    else:
        print("Неизвестная команда.")
    command = input("Введите команду: ")
    
