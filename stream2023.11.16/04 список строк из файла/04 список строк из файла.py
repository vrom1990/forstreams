file = open("data.txt", "r", encoding="utf-8")
lines_list = file.readlines()
file.close()
for i, line in enumerate(lines_list):
    lines_list[i] = line.strip()
print(lines_list)