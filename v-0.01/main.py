from Classes.DB import DB
from Classes.todo import ToDo


try:
    conn_db = DB()
    newToDo = ToDo()
    newToDo.db = conn_db
    newToDo.start()

finally:
    conn_db.conn.close()
