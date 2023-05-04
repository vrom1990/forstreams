'''
Задание: проверить, есть ли в наборе элементов слово «молоко»
'''
# решение без списков
'''
n = int(input("Сколько элементов? "))
nashli = False

for step in range(n):
    element = input("Введите элемент набора: ")
    if element == "молоко":
        nashli = True
        break
    
if nashli == True:
    print("Молоко есть в наборе")
else:
    print("Молоко отсутствует в наборе")
    
'''

#решение через списки

spisok = ["чай", 1, "самовар","молоко", "печенье", "клубника"]
nashli = False
for element in spisok:
     if element == "молоко":
        nashli = True
        break
    
if nashli == True:
    print("Молоко есть в наборе")
else:
    print("Молоко отсутствует в наборе")