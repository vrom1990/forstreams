from time import sleep

def pprint(*strList, end="\n", sep=" "):
    lastIndex = len(strList)-1
    for i,string in enumerate(strList):
        for letter in string:
            print(letter, end="")
            sleep(0.1)
        if i != lastIndex:
            print(end=sep)
    print(end=end)

text = input("Введите текст: ")
pprint("Введёный текст:", text,", вот!", sep = "[]", end = "===>\n")

