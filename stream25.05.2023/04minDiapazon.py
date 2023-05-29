'''
Найти в наборе максимальное число, которое не меньше 0 и
не больше 20. Если таких чисел нет, написать «Их нет».

'''

# Решение без списков

'''
n = int(input("Количество элементов: "))

maximum = -1

for step in range(n):
    num = float(input("Введите число: "))
    if num > maximum and num >= 0 and num <= 20 :
        maximum = num


if maximum == -1:
    print("Их нет")
else: 
    print("Максимум:", maximum)
    
'''

# Решение через списки


spisok = [-1, 2, -40, -0.5, 21, 12, 50]
maximum = -1

for num in spisok:
    if num > maximum and num >= 0 and num <= 20 :
        maximum = num


if maximum == -1:
    print("Их нет")
else: 
    print("Максимум:", maximum)