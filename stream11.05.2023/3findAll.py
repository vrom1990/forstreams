"""
Найдите в наборе все температуры меньше нуля
и выведите их номера на экран
"""

# Решение 1
'''
n = int(input("Введите количество: "))
minusa = []

for step in range(1, n+1):
    t = float(input("Введите температуру: "))
    if t < 0:
        minusa.append(step)

if len(minusa) == 0:
    print("Не было критических понижений")
else:
    print(minusa)
'''

temperatury = [1, 20, 3, 2, 7, 1, 6]
minusa = []

for i in range(len(temperatury)):
    if temperatury[i] < 0:
        minusa.append(i+1)

if len(minusa) == 0:
    print("Не было критических понижений")
else:
    print(minusa)