with open("date.txt", "r", encoding="utf-8") as file:
    print(file.read())

new_text = input("Введите новый текст: ")

with open("date.txt", "w", encoding="utf-8") as file:
    file.write(new_text)