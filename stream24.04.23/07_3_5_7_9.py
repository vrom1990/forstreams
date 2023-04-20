"""
3 5 7 9 11 13...
сколько введёт пользователь
"""

# первое решение
n = int(input("Введите количество: "))

for step in range(1, n+1):
    print(step*2+1, end=" ")


'''
# второе решение
n = int(input("Введите количество: "))

for step in range(2, n+2):
    print(step*2-1, end=" ")
'''

'''
#третье решение

n = int(input("Введите количество: "))

for step in range(4, 2*n+4, 2):
    print(step-1, end=" ")
'''