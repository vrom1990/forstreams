'''
Вывести n элементов:
#-#-#-#-#-#-#-#-#-#-#-#-#-
'''

n = int(input("Введите количество: "))

for step in range(1, n+1):
    if step%2 == 1:
        print("#", end="")
    else:
        print("-", end="")