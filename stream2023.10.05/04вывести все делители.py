def deliteli(n):
    delList = [1]
    for num in range(2, n // 2+1):
        if n % num == 0:
            delList.append(num)
    delList.append(n)
    return delList

num = int(input("Введите число: "))
myList = deliteli(num)
print(*myList)