"""
Отфильтровать набор целых чисел, выбрать только те,
которые не делятся на 6, вывести получившийся список
"""

# Решение 1, получаем из командной строки
"""
n = int(input("Сколько чисел?: "))
spisokF = []

for step in range(n):
    num = int(input("Введите число: "))
    if num % 6 > 0:
       spisokF.append(num)
       
print(spisokF)
"""

# Решение 2, получаем из списка

spisok = [1, 18, 0, 11, 12, 53, 74, 12, 6]
spisokF = []

for num in spisok:
    if num % 6 > 0:
        spisokF.append(num)

print(spisokF)
