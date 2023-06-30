texts = ["побрить руку", "опровергнуть теорему Пифагора", "построить гигантского робота","побыть гусём", "получить акциии МММ"]
categories = ["красоста", "работа", "хобби", "работа", "работа"]

print("Добро пожаловать в менеджер задач")
print()
print("ЗАДАЧИ")
for i in range(len(texts)):
        print(i+1, texts[i], "|",categories[i])
        
command = input("введите команду: ")
while command != "выход":
    if command == "добавить":
        new_task = input("Введите текст новой задачи: ")
        new_task_ctgr = input("Введите категорию: ")
        texts.append(new_task)
        categories.append(new_task_ctgr)
    elif command == "изменить":
        input_text = "Введите номер задачи, которую хотите отредактировать: "
        index = int(input(input_text)) - 1
        if index >= 0 and index < len(texts):
            pole = input("Какое поле редактируем? ")
            if pole == "текст":
                texts[index] = input("Введите новый текст задачи: ")
            elif pole == "категория":
                categories[index] = input("Введите категорию: ")
            elif pole == "отмена":
                print("Операция отменена")
            else:
                print("Такого поля нет")
        else:
            print("Нет такого номера")
    elif command == "удалить":
        input_text = "Введите номер задачи, которую хотите удалить: "
        index = int(input(input_text)) - 1
        if index >= 0 and index < len(texts):
            texts.pop(index)
            categories.pop(index)
        else:
            print("Нет такого номера")
    elif command == "фильтр":
        pole = input("по какому полю фильтруем: ")
        if pole == "категория":
            category = input("Введите категорию: ")
            print("Задачи с категорией '", category, "'", sep="")
            if category in categories:
                for i in range(len(texts)):
                    if categories[i] == category:
                        print(i+1, texts[i], "|",categories[i])
                print()
            else:
                print("отсутствуют.")
                print()
        else:
            print("неверное поле фильраци")
    else:
        print("Неизвестная команда")
    
    
    print("ЗАДАЧИ")
    for i in range(len(texts)):
        print(i+1, texts[i], "|",categories[i])
        
    command = input("введите команду: ")
    
print("Менеджер задач выключен")
