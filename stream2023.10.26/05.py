from time import sleep

def pprint(*strList, sep=" ", end="\n"):
    for string in strList:
        for letter in string:
            print(letter, end="")
            sleep(0.1)
        print(end=sep)
    print(end=end)

text = input("Введите текст: ")
pprint("Введёный текст:", text,", вот!", sep = "[]", end = "===>\n")
