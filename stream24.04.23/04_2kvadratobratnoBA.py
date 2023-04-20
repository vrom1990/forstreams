A = int(input("Введите A: "))
B = int(input("Введите B: "))

for step in range(B, A-1, -1):
    print(2 * step**2)