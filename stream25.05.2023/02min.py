"""
Найти минимальное число в наборе
"""
# Решение без списков

"""
n = int(input("Количество элементов: "))

minimum = 0

for step in range(n):
    num = int(input("Введите число: "))
    if step == 0 or num < minimum:
        minimum = num


print("Минимум:", minimum)
"""
# Решение через списки

spisok = [3, 5, -1, -8, 4, 8, 2]
minimum = spisok[0]

for num in spisok:
    if num < minimum:
        minimum = num

print("Минимум:", minimum)

