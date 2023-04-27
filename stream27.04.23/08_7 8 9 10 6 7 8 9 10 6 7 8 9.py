'''
Вывести n элементов:
7 8 9 10 6 7 8 9 10 6 7 8 9
'''

n = int(input("Введите количество: "))
for step in range(1, n+1):
    print(step % 5 + 6, end=" ")

