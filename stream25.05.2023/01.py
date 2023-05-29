"""
Найти максимальное число в наборе
"""
# Решение без списков

"""
n = int(input("Количество элементов: "))

maximum = 0

for step in range(n):
    num = int(input("Введите число: "))
    if step == 0 or num > maximum:
        maximum = num


print("Максимум:", maximum)
"""
# Решение через списки

spisok = [3, 5, -1, -8, 4, 8, 2]
maximum = spisok[0]

for num in spisok:
    if num > maximum:
        maximum = num

print("Максимум:", maximum)
