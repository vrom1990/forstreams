class Account_list:
    def __init__(self, acc_list):
        self.list = acc_list
    def add(self):
        login = input("Введите логин: ")
        passwd = input("Введите пароль: ")
        email = input("Введите почту: ")
        phone = input("Введите номер телефона: ")
        name = input("Введите отображаемое имя: ")
        self.list.append(Account(login, passwd, email, phone, name))
        self.print()
        
    def print(self):
        print("логин", "пароль", "email", "телефон", "имя")
        for acc in self.list:
            print(acc.login, acc.passwd, acc.email, acc.phone, acc.name)
            
    def change(self):
        login = input("Введите логин: ")
        i = -1
        for index, acc in enumerate(self.list):
            if login == acc.login:
                i = index
                break 
        self.list[i].change()
        self.print()
    def remove(self):
        login = input("Введите логин: ")
        i = -1
        for index, acc in enumerate(self.list):
            if login == acc.login:
                i = index
                break 
        self.list.pop(i)
        self.print()
    def main(self):
        self.print()
        command = input("Введите команду: ")

        while command != "выход":
            if command == "добавить":
                self.add()
            elif command == "изменить":
                self.change()
            elif command == "удалить":
                self.remove()
            else:
                print("Неизвестная команда")
            command = input("Введите команду: ")
    
    
class Account:
    def __init__(self, login, passwd, email, phone, name):
        self.login = login
        self.passwd = passwd
        self.email = email
        self.phone = phone
        self.name = name
    def change(self):
        print("Вы меняете аккаунт", self.login)
        pole = input("Какое поле хотите изменить?: ")
        while pole not in ["логин", "пароль", "почта", "телефон", "имя", "отмена"]:
            print("Такого поля нет! Введите существующее поле или слово «отмена»")
            pole = input("Какое поле хотите изменить?: ")
        if pole != "отмена":
            if pole == "логин":
                self.login = input("Введите новый логин: ")
            elif pole == "пароль":
                self.passwd = input("Введите новый пароль: ")
            elif pole == "почта":
                self.email = input("Введите новую почту: ")
            elif pole == "телефон":
                self.phone = input("Введите новый телефон: ")
            elif pole == "имя":
                self.name = input("Введите новый имя: ")
        else:
            print("Изменение аккаунта отменено!")
    
    


accs= [Account("ser123", "123456", "mylo@mail.com", "777", "Сергей"),
            Account("ann111", "123456p", "ann111@mail.com", "88005553535", "Анечка"),
            Account("kega", "123456789", "kegakega@mail.com", "111", "Кега")]
accounts = Account_list(accs)

accounts.main()
