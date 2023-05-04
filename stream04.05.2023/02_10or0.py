'''
Проверьте и сообщите:
есть ли в наборе целых чисел число 10 или 0
'''
# Решение без списков
'''
n = int(input("Сколько элементов? "))
nashli = False

for step in range(n):
    element = input("Введите элемент набора: ")
    if element == "10" or element == "0":
        nashli = True
        break
    
if nashli == True:
    print("10 или 0 есть в наборе")
else:
    print("10 или 0 отсутствует в наборе")
    

'''
# Решение через списки

spisok = [2, 0, 1, 7, 12, 5, 9]
nashli = False
for element in spisok:
     if element == 10 or element == 0:
        nashli = True
        break
    
if nashli == True:
    print("Молоко есть в наборе")
else:
    print("Молоко отсутствует в наборе")
