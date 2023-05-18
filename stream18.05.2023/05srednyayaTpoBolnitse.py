'''
Посчитать среднее арифметическое температур
от 36 до 37 включительно
'''
'''
#Решение без списков
n = int(input("Введите количество температур: "))
kolichestvo = 0
summa = 0

for step in range(n):
    t = float(input("Введите температуру: "))
    if 36 <= t and t <= 37:
        kolichestvo = kolichestvo + 1
        summa = summa + t
        
sredneye = summa / kolichestvo
        
print("Средняя температура по больнице среди здоровых", sredneye)


'''

#Решение через список
spisokT = [35, 36.5, 36, 37, 39]
kolichestvo = 0
summa = 0

for t in spisokT:
    if 36 <= t and t <= 37:
        kolichestvo = kolichestvo + 1
        summa = summa + t
        
sredneye = summa / kolichestvo
        
print("Средняя температура по больнице среди здоровых", sredneye)