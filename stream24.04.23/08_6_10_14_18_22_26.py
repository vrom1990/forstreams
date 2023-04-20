"""
6 10 14 18 22 26 30... 
сколько введёт пользователь
"""
'''
# первое решение
n = int(input("Введите количество: "))

for step in range(1, n+1):
    print(step*4+2, end=" ")
'''

# второе решение

n = int(input("Введите количество: "))

for step in range(6, 4*n+6, 4):
    print(step, end=" ")
