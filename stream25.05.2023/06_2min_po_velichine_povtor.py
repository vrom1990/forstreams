"""
Найти второе минимильное по величине число в наборе,
числа могут повторяться
"""

spisok = [1, 3, 3, 3]

minimum = spisok[0]
maximum = spisok[0]

for num in spisok:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num


if maximum == minimum:
    print("Все числа в наборе одинаковые")
else:
    minimum2 = maximum
    for num in spisok:
        if num < minimum2 and num != minimum:
            minimum2 = num
    print("Второй минимум:", minimum2)
