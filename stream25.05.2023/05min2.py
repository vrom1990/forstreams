'''
Найти число в наборе из неповторяющихся элементов, которое будет минимальным,
если убрать из набора минимальное число
'''

spisok = [6, 6, 12, 10, 50, 70]

minimum = spisok[0]
minimum2 = spisok[0]

for num in spisok:
    if num < minimum:
        minimum = num


if minimum == spisok[0]:
    minimum2 = spisok[1]


for num in spisok:
    if num < minimum2 and num != minimum:
        minimum2 = num

print("Второй минимум:", minimum2)
