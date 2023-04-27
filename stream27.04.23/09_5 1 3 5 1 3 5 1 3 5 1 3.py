'''
Вывести n элементов:
5 1 3 5 1 3 5 1 3 5 1 3 
'''
'''
# решение 1

n = int(input("Введите количество: "))
for step in range(1, n+1):
    if step % 3 == 1:
        print(5, end=" ")
    elif step % 3 == 2:
        print(1, end=" ")
    else:
        print(3, end=" ")
        
'''
#решение 2

n = int(input("Введите количество: "))
for step in range(2, n+2):
    print(step % 3 * 2 + 1 , end=" ")