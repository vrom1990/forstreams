"""
тест

"""
"""
#Если номер ряда равен номеру колонки

for row in range(1, 10):
    for column in range(1, 10):
        if row == column:
            print('#', end="")
        else:
            print('*', end="")
        
    print()
"""

#Если номер ряда равен номеру колонки +(или -) — подставьте разное число

for row in range(1, 10):
    for column in range(1, 10):
        if row == column - 3:
            print('#', end="")
        else:
            print('*', end="")
        
    print()


"""
# Если номер ряда меньше номера колонки

for row in range(1, 10):
    for column in range(1, 10):
        if row < column:
            print('#', end="")
        else:
            print('*', end="")
        
    print()
    
"""
"""
# Если номер ряда больше номера колонки
for row in range(1, 10):
    for column in range(1, 10):
        if row > column:
            print('#', end="")
        else:
            print('*', end="")
        
    print()
"""
"""
# Если сумма больше... (подставляем разные числа)
for row in range(1, 10):
    for column in range(1, 10):
        if row+column <= 10:
            print('#', end="")
        else:
            print('*', end="")
"""

"""
# Если сумма равна... (подставляем разные числа)
for row in range(1, 10):
    for column in range(1, 10):
        if row + column == 8:
            print("#", end="")
        else:
            print("*", end="")

    print()
"""