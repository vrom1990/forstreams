'''
Вывести n элементов:
1 -1 1 -1 1 -1 1 -1 1 -1
'''

n = int(input("Введите количество: "))

for step in range(1, n+1):
    if step % 2 == 1:
        print(1, end=" ")
    else:
        print(-1, end=" ")