"""
Найти максимальное число в наборе положительных чисел
"""
# Решение без списков


n = int(input("Количество элементов: "))

maximum = -1

for step in range(n):
    num = float(input("Введите число: "))
    if num > maximum:
        maximum = num


print("Максимум:", maximum)
