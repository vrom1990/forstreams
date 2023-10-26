from time import sleep

def pprint(*strList):
    for string in strList:
        for letter in string:
            print(letter, end="")
            sleep(0.3)
        print(" ",end="")

text = input("Введите текст: ")
pprint("Введёный текст:", text,", вот!")