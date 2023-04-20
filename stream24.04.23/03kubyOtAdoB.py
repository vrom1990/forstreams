A = int(input("Введите A: "))
B = int(input("Введите B: "))

print("A:", A)
print("B:", B)
for step in range(A, B+1):
    print(step, "в кубе =", step**3)

