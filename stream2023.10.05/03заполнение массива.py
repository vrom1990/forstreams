'''
Создать и использовать подпрограммы
для генерации списка из случайных чисел,
списка чисел, введённых из консоли
и вывода списка

'''

import random

def buildRandomList(n, minE, maxE):
    thisList = []
    for step in range(n):
        thisList.append(random.randint(minE,maxE))
    return thisList

def buildInputList(n):
    thisList = []
    for step in range(n):
        thisList.append(int(input("Введите число: ")))
    return thisList

def printList(thisList):
    for elem in thisList:
        print(elem, end=" ")
    print()

randomList = buildRandomList(10, 1, 10)
inputList = buildInputList(5)
printList(randomList)
printList(inputList)
    
