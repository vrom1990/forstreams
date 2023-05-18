'''
Чему равно произведение элементов в наборе?
'''
'''
#Решение без списков
n = int(input("Введите количество элементов: "))
proizvedenije = 1

for step in range(n):
    num = int(input("Введите число: "))
    proizvedenije = proizvedenije * num
   
        
print("Произведение всех элементов: ", proizvedenije)
'''

#Решение через список
spisok= [1, 2, 3, 4, 5]
proizvedenije = 1

for num in spisok:
    proizvedenije = proizvedenije * num
   
        
print("Произведение всех элементов: ", proizvedenije)