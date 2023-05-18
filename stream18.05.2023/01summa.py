'''
Найти сумму чисел в наборе
'''

'''
# Решение без списков
n = int(input("Введите количество: "))
summa = 0


for step in range(n):
    num = float(input("Введите число: "))
    summa = summa + num

print("Сумма чисел:",summa)
'''
# Решение через списки

spisok = [1, 7, 2, 2, 3]
summa = 0

for num in spisok:
    summa = summa + num

print("Сумма чисел:", summa)