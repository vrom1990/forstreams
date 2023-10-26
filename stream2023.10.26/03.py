from time import sleep

def pprint(pText):
    for letter in pText:
        print(letter, end="")
        sleep(0.3)

text = input("Введите текст: ")
pprint(text)

