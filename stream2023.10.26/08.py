from time import sleep

def pprint(*argList, end="\n", sep=" "):
    lastIndex = len(argList)-1
    for i,arg in enumerate(argList):
        if isinstance(arg, str):
            string = str(arg)
        else:
            string = arg
        for letter in str(arg):
            print(letter, end="")
            sleep(0.1)
        if i != lastIndex:
            print(end=sep)
    print(end=end)

text = input("Введите текст: ")
pprint("Текст:", text,", вот!",1 ,"штук!", sep = "--", end = "!!!\n")



