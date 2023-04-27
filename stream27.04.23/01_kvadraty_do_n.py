'''
Вывести все квадраты натуральных чисел, не превосходящие данного числа N.

Например, если N = 50, то на экран должен быть выведен ряд 1 4 9 16 25 36 49.
'''

'''
#решение 1
n = int(input("Введите максимальное возможное число для последовательности: "))

for step in range(1, n+1):
    if step*step > n:
        break
    else:
        print(step*step, end=" ")
        
'''

#решение 2
from math import sqrt, floor

n = int(input("Введите максимальное возможное число для последовательности: "))

sqrt_n = floor(sqrt(n))

for step in range(1, sqrt_n+1):
    print(step*step, end=" ")