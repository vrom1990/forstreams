file = open("data.txt", "r", encoding="utf-8")
for string in file:
    print(string.strip())
file.close()

date = input("Внесите дату: ")
time = input("Внесите время: ")
t = input("Внесите температуру: ")

file = open("data.txt", "a", encoding="utf-8")
new_line = "\n" + date + " " + time + " температура " + t
file.write(new_line)
file.close()