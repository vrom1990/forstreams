
#Открыть файл, прочитать и закрыть
file = open("names.txt", "r", encoding="utf-8")
print(file.read())
file.close()
'''
#Открыть файл, перезаписать и закрыть
file = open("names.txt", "w", encoding="utf-8")
file.write("Вот текст")
file.close()
'''
'''
#Открыть файл, дозаписать и закрыть
file = open("names.txt", "a", encoding="utf-8")
file.write("\nДобавленный текст")
file.close()
'''

