'''
Задача: проверить в наборе температур,
не было ли понижения. Если понижение температур было, то написать:
мальчик филонит
иначе написать:
мальчик старается
'''

spisokT = [2, 3, 3, 12, 10, 15, 16]
ponijenije = False

for index in range(len(spisokT) - 1):
    if spisokT[index] > spisokT[index+1]:
        ponijenije = True
        break
if ponijenije == True:
    print("мальчик филонит")
else:
    print("мальчик старается")
    