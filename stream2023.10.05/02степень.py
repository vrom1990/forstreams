'''
Составить программу вычисления
данного выражения: y = (x^6*(x-5)^3) / (2*x+1)^5.
'''

def power(num, powerNum):
    result = 1
    for step in range(powerNum):
        result *= num
    return result
  
x = float(input("Введите x: "))

a = power(x, 6)
b = power(x-5, 3)
c = power(2*x+1, 5)

y = round((a * b / c)*10000)/10000
print(y)


