login_file = open("loginparol.txt", "r", encoding="utf-8")
CORRECT_LOGIN = login_file.readline().strip()
CORRECT_PAROL = login_file.readline()
login_file.close()

login = input("Введите логин: ")
parol = input("Введите пароль: ")

if login == CORRECT_LOGIN and parol == CORRECT_PAROL:
    print("Поздравляю с успешным входом!")
    print("Что хотите сделать?")
    command = input("показать данные(1) или изменить логин/пароль(2): ")
    if command == "1":
        data_file = open("secretdata.txt", "r", encoding="utf-8")
        print(data_file.read())
        data_file.close()
    
    elif command == "2":
        new_login = input("Введите новый логин: ")
        new_parol = input("Ведите новый пароль: ")
        login_file = open("loginparol.txt", "w", encoding="utf-8")
        login_file.write(new_login)
        login_file.write("\n" + new_parol)
        login_file.close()
    
    else:
        print("Такого варианта нет!")
        print("Доступ закрыт.")
else:
    print("Неверные данные!")
    print("Доступ закрыт.")