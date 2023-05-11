'''
Найти в заданном наборе данных строку «молоко»
(она одна) и вывесте, под каким номером она в наборе
'''

#решение 1
'''
n = int(input("Введите количество: "))
number = -1

for step in range(1, n+1):
    word = input("Введите слово: ")
    if word == "молоко":
        number = step
        break

if number == -1:
    print("Не найдено")
else:
    print("Молоко находится под номером", step)
'''

#решение 2 через списки
spisok = ["огонь", "вода", "молоко", "земля", "небо", "кефирчик", "БООООООРЩ"]
nomer = -1

for i in range(len(spisok)):
    if spisok[i] == "молоко":
        nomer = i + 1
        break

if nomer == -1:
    print("Не найдено")
else:
    print("Молоко находится под номером", nomer)