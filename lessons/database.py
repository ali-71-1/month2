# sqlite3 — встроенный модуль Python для работы с базами данных SQLite
import sqlite3


# создаёт таблицу students, если её ещё нет
def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    """)

# добавляет одного студента в таблицу
def add_student(conn, name, age, city):
    # знаки ? — места подстановки: Python сам подставит значения из кортежа.
    # Значения передаются отдельно от текста запроса — защита от SQL-инъекций.
    conn.execute("""
    INSERT INTO students
    VALUES (?, ?, ?)
    """, (name, age, city)
    )
    # без commit() изменения не сохранятся в файле базы данных
    conn.commit()


if __name__ == '__main__':
    # подключаемся к файлу базы (файл создастся, если его ещё нет)
    connection = sqlite3.connect('database.db') # DataBase
    create_tables(connection)
    add_student(connection, "Igor", 22, "Bishkek")
    add_student(connection, "Arzybek", 26, "Sokuluk")
    add_student(connection, "Ali", 18, "Osh")
    # закрываем соединение с базой
    connection.close()
