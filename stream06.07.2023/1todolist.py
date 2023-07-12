texts = ["побрить руку", "опровергнуть теорему Пифагора",
         "построить гигантского робота","побыть гусём", "получить акциии МММ"]
categories = ["красоста", "работа", "хобби", "работа", "работа"]
vajnosti = ["важно", "средне", "важно", "важно", "неважно"]
srochnosti = ["срочно", "средне", "не срочно", "не срочно", "срочно"]
vypolnenosti = [False, False, False, False, False]
print("Добро пожаловать в менеджер задач")
print()
print("ЗАДАЧИ")
for i in range(len(texts)):
    if vypolnenosti[i]:
        vypolnenost = "✓"
    else:
        vypolnenost = "⨷"
    print(i+1, texts[i], "|",categories[i], "|",
          vajnosti[i], "|", srochnosti[i], "|", vypolnenost)
    
command = input("введите команду: ")
while command != "выход":
    if command == "добавить":
        new_task = input("Введите текст новой задачи: ")
        new_task_ctgr = input("Введите категорию: ")
        new_vajnost = input("Введите важность задачи: ")
        while not(new_vajnost in ["важно", "средне", "неважно"]):
            print("Недопустимое значение")
            new_vajnost = input("Введите важность задачи: ")
        new_srochnost = input("Введите срочность задачи: ")
        while not(new_srochnost in ["срочно", "средне", "не срочно"]):
            print("Недопустимое значение")
            new_srochnost = input("Введите срочность задачи: ")
        texts.append(new_task)
        categories.append(new_task_ctgr)
        vajnosti.append(new_vajnost)
        srochnosti.append(new_srochnost)
        vypolnenosti.append(False)
    elif command == "изменить":
        input_text = "Введите номер задачи, которую хотите отредактировать: "
        index = int(input(input_text)) - 1
        if index >= 0 and index < len(texts):
            pole = input("Какое поле редактируем? ")
            if pole == "текст":
                texts[index] = input("Введите новый текст задачи: ")
            elif pole == "категория":
                categories[index] = input("Введите категорию: ")
            elif pole == "важность":
                new_vajnost = input("Введите новую важность задачи: ")
                while not(new_vajnost in ["важно", "средне", "неважно"]):
                    print("Недопустимое значение")
                    new_vajnost = input("Введите новую важность задачи: ")
                vajnosti[index] = new_vajnost
            elif pole == "срочность":
                new_srochnost = input("Введите новую срочность задачи: ")
                while not(new_srochnost in ["срочно", "средне", "не срочно"]):
                    print("Недопустимое значение")
                    new_srochnost = input("Введите новую срочность задачи: ")
                srochnosti[index] = new_srochnost
            elif pole == "отмена":
                print("Операция отменена")
            else:
                print("Такого поля нет")
        else:
            print("Нет такого номера")
    elif command == "пометить":
        input_text = "Введите номер задачи, которую хотите отредактировать: "
        index = int(input(input_text)) - 1
        if index >= 0 and index < len(texts):
            if vypolnenosti[index]:
                print("Задача '", texts[index], "' помечена как невыполненная", sep="")
                vypolnenosti[index] = False
            else:
                print("Задача '", texts[index], "' помечена как выполненная", sep="")
                vypolnenosti[index] = True
        else:
            print("Неверный индекс")
    elif command == "удалить":
        input_text = "Введите номер задачи, которую хотите удалить: "
        index = int(input(input_text)) - 1
        if index >= 0 and index < len(texts):
            texts.pop(index)
            categories.pop(index)
            vajnosti.pop(index)
            srochnosti.pop(index)
            vypolnenosti.pop(index)
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
                        if vypolnenosti[i]:
                            vypolnenost = "✓"
                        else:
                            vypolnenost = "⨷"
                        print(i+1, texts[i], "|",categories[i], "|",
                              vajnosti[i], "|", srochnosti[i], "|", vypolnenost)
                print()
            else:
                print("отсутствуют.")
                print()
        elif pole == "срочность":
            srochnost = input("Введите срочность:")
            if srochnost in ["срочно", "средне", "не срочно"]:
                print("Задачи со срочностью '", srochnost, "':", sep="")
                for i in range(len(texts)):
                    if srochnosti[i] == srochnost:
                        if vypolnenosti[i]:
                            vypolnenost = "✓"
                        else:
                            vypolnenost = "⨷"
                        print(i+1, texts[i], "|",categories[i], "|",
                              vajnosti[i], "|", srochnosti[i], "|", vypolnenost)
            else:
                print("Таких задач нет.")
        elif pole == "важность":
            vajnost = input("Введите важность:")
            if vajnost in ["важно", "средне", "неважно"]:
                print("Задачи с важностью '", vajnost, "':", sep="")
                for i in range(len(texts)):
                    if vajnosti[i] == vajnost:
                        if vypolnenosti[i]:
                            vypolnenost = "✓"
                        else:
                            vypolnenost = "⨷"
                        print(i+1, texts[i], "|",categories[i], "|",
                              vajnosti[i], "|", srochnosti[i], "|", vypolnenost)
            else:
                print("Таких задач нет.")
        else:
            print("неверное поле фильраци")
    elif command == "вывести":
        print("ЗАДАЧИ")
        for i in range(len(texts)):
            if vypolnenosti[i]:
                vypolnenost = "✓"
            else:
                vypolnenost = "⨷"
            print(i+1, texts[i], "|",categories[i], "|",
                  vajnosti[i], "|", srochnosti[i], "|", vypolnenost)
    else:
        print("Неизвестная команда")
    
    
    
        
    command = input("введите команду: ")
    
print("Менеджер задач выключен")
