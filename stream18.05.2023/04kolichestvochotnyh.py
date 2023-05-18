'''
посчитать количество всех чётных чисел в случайном наборе
'''

from random import randrange
n = int(input("Введите количество элементов: "))
kolichestvo = 0
spisok = []
for i in range(n):
    spisok.append(randrange(0,22))
print(spisok)

for num in spisok:
    if num % 2 == 0:
        kolichestvo = kolichestvo + 1

print("Чётных чисел в наборе", spisok)
print(kolichestvo, "штук")
