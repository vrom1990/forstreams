from time import sleep

text = input("Введите текст: ")

for letter in text:
    print(letter, end="")
    sleep(0.3)