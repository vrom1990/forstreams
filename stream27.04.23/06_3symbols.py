'''
Вывести n элементов:
%*0%*0%*0%*0%*0%*0%*0%*0%*0
'''

n = int(input("Введите количество: "))

for step in range(1, n+1):
    if step % 3 == 1:
        print("%", end="")
    elif step % 3 == 2:
        print("*", end="")
    else:
        print("0", end="")
