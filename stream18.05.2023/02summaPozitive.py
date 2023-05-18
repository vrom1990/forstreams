'''
Найти сумму положительных чисел в наборе
'''

'''
# Решение без списков
n = int(input("Введите количество: "))
summa = 0


for step in range(n):
    num = float(input("Введите число: "))
    if num > 0:
        summa = summa + num

print("Сумма чисел:",summa)
'''
# Решение через списки

spisok = [1, 7,0,  2, -6, 2, 3, -8]
summa = 0

for num in spisok:
    if num > 0:
        summa = summa + num

print("Сумма чисел:", summa)