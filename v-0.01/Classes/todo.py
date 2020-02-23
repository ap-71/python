class ToDo:
    toDoList = {}
    db = object

    def start(self):
        # self.count += 1
        while True:
            action = "get"
            self.db.exec_db(action)
            print("""
--------------------------------------
ИД     | Задание
--------------------------------------""")
            for i in self.db.tmp_tasks:
                print(f"{i[0]}          {i[2] + ' -- ' + i[1] + ' -- ' + i[3]}")
            print("--------------------------------------")
            print("1: Добавить задание")
            print("2: Удалить задание")
            # print("4: Посмотреть число пользователей")
            inp: str = input("=> ")
            if inp == "1":
                action = "add"
                while True:
                    date = input("Дата: ")
                    title = input("Название: ")
                    description = input("Описание: ")
                    check = input("Верно Y/n?")
                    if check == "n" or check == "N":
                        continue
                    else:
                        self.db.exec_db(action, tmp_title=title, tmp_date=date, tmp_description=description)
                        break
            elif inp == "2":
                action = "del"
                id = input("Введите ID задания: ").split(" ")
                for tmp_id in id:
                    self.db.exec_db(action, tmp_id=tmp_id)
            # elif inp == "4":
            #     print(f"Число пользователей: {self.count}")
            else:
                print("ничего не ввели")
