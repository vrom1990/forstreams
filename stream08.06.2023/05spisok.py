'''
Найди, на каком месте(номер) находится слово «молоко» в наборе слов.
Слово «молоко» может встретиться максиму один раз, а может не встретиться,
тогда об этом нужно сообщить
'''
'''
#Решение через for
spisok = ["хлеб", "кефир", "яблоко", "вафли"]
nomer = -1

for i in range(len(spisok)):
    if spisok[i] == "молоко":
        nomer = i + 1
        break

if nomer > -1:
    print("Молоко на", nomer, "месте.")
else:
    print("Молока нет")
'''

#Решение через while
spisok = ["хлеб", "кефир", "молоко", "яблоко", "вафли"]
nomer = -1

i = 0
n = len(spisok)
while i < n:
    if spisok[i] == "молоко":
        nomer = i + 1
        break
    i = i + 1

if nomer > -1:
    print("Молоко на", nomer, "месте.")
else:
    print("Молока нет")
