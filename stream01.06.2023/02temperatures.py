"""
Отфильтровать набор температур и оставить только те, которые
или меньше 0, или больше 35,вывести получившийся список
"""

# Решение 1, получаем данные из командной строки
"""
n = int(input("Сколько температур?: "))
spisokF = []

for step in range(n):
    t = float(input("Введите температуру: "))
    if t < 0 or t > 35:
        spisokF.append(t)
    
print(spisokF)
"""
# Решение 2, получаем данные из списка

spisokT = [1, 5, 23, 30, -10, 35, 0, 50, 2]
spisokF = []

for t in spisokT:
    if t < 0 or t > 35:
        spisokF.append(t)

print(spisokF)
