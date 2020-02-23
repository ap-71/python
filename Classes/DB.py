import sqlite3


class DB:
    nameDB = "todo"
    conn = sqlite3.connect("DB/todo.db")
    tmp_tasks = {}

    def exec_db(self, action, tmp_title="NULL", tmp_date="NULL", tmp_description="NULL", tmp_id="NULL"):
        cursor = self.conn.cursor()
        cursor.execute(f"""create table if not exists {self.nameDB} (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title text, date text, description text)""")
        if action == "add" or action == "del":
            if action == "add":
                cursor.execute(f"""INSERT INTO {self.nameDB}
                                  VALUES (NULL, '{tmp_title}', '{tmp_date}',
                                  '{tmp_description}')""")
            elif action == "del":
                cursor.execute(f"DELETE FROM {self.nameDB} WHERE id = '{tmp_id}'")
            self.conn.commit()
        elif action == "get":
            cursor.execute(f"SELECT * FROM {self.nameDB}")
            self.tmp_tasks = cursor.fetchall()
        cursor.close()