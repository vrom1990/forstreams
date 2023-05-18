'''
Посчитать количество температур в наборе температур, котрые
не ниже -5 и не выше +5
'''
'''
#Решение без списков
n = int(input("Введите количество элементов: "))
kolichestvo = 0
for step in range(n):
    t = float(input("Введите температуру: "))
    if -5 <= t and t <= 5:
        kolichestvo = kolichestvo + 1
        
print("Близость к нулевой температуре зафиксирована", kolichestvo, "раз.")
'''

#Решение через списки
spisokT = [4, 5, -20, 30, 4.9, 5.001, 0.1, -5.0001]
kolichestvo = 0
for t in spisokT:
    if -5 <= t and t <= 5:
        kolichestvo = kolichestvo + 1
        
print("Близость к нулевой температуре зафиксирована", kolichestvo, "раз.")