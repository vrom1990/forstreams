#Считать несколько строк по очереди

file = open("data.txt", "r", encoding="utf-8")
print(file.readline().strip())
print(file.readline().strip())
print(file.readline())