"""
Задание: напишите, можно ли из того, что есть в наборе,
сделать бутерброд с маслом. Если в наборе есть и хлеб и масло,
то программи должна сообщить: бутерброд сделать можно. Иначе:
бутерброд сделать нельзя
"""

#решение без списков
'''
n = int(input("Сколько элементов? "))
nashliHleb = False
nashliMaslo = False
for step in range(n):
    element = input("Введите элемент набора: ")
    if element == "масло":
        nashliMaslo = True
    if element == "хлеб":
        nashliHleb = True
    if nashliMaslo == True and nashliHleb == True:
        break
    
    
if nashliMaslo == True and nashliHleb == True:
    print("бутерброд сделать можно")
else:
    print("бутерброд сделать нельзя")
    
'''

rukzak = ["чай", "варенье", "масло", "хлеб", "молоко", "колбаса"]
nashliHleb = False
nashliMaslo = False
for element in rukzak:
    if element == "масло":
        nashliMaslo = True
    if element == "хлеб":
        nashliHleb = True
    if nashliMaslo == True and nashliHleb == True:
        break
    
    
if nashliMaslo == True and nashliHleb == True:
    print("бутерброд сделать можно")
else:
    print("бутерброд сделать нельзя")