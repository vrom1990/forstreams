"""
Посчитайте среднее арифметическое для набора целых чисел.
Перед набором чисел идёт количество этих чисел
"""

'''
#Решение через for
summa = 0
n = int(input("Введите количество: "))

for step in range(n):
    num = int(input("Введите число: "))
    summa = summa + num
    
print(summa/n)
'''

summa = 0
n = int(input("Введите количество: "))
step = 1

while step <= n:
    num = int(input("Введите число: "))
    summa = summa + num
    step = step + 1
    
print(summa/n)