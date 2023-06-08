'''
Программа получает от датчика температуру снова и снова 10 раз.
Если температура упадёт ниже нуля, то программа
сообщит "ТРЕВОГА" и завершит работу. Иначе ничего не сообщит.
'''
'''
#Решение 1 While
t = int(input("Введите температуру: "))
step = 1


while t >= 0 and step < 10:
    t = int(input("Введите температуру: "))
    step = step + 1

if t < 0:
    print("ТРЕВОГА")
    
'''

#Решение 2 While и break
step = 1

while step <= 10:
    t = int(input("Введите температуру: "))
    if t < 0:
        print("ТРЕВОГА")
        break
    
    step = step + 1


#Решение через for
    
for step in range(10):
    t = int(input("Введите температуру: "))
    if t < 0:
        print("ТРЕВОГА")
        break