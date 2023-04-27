'''
Вывести n элементов:
0 3 6 9 0 3 6 9 0 3 6 9
'''

#решение 1
n = int(input("Введите количество элементов: "))
for step in range(1, n+1):
    print((step+3) % 4 * 3, end=" ")
    
#решение 2
    
for step in range(4, n+4):
    print(step % 4 * 3, end=" ")