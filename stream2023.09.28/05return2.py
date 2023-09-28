def otsenka(spisok):
    kol_vo = len(spisok)
    summa = 0
    for num in spisok:
        summa += num
    srednee = summa/kol_vo
    if srednee >= 4:
        return "Здорово!"
    else:
        return "Ну такое"

spisok_otsenok = []
num = input("Введите оценку: ")
while num != "стоп":
    spisok_otsenok.append(int(num))
    num = input("Введите оценку: ")
    
print(otsenka(spisok_otsenok))