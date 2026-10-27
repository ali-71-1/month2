import sqlite3
def create_tables(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS car (
    name TEXT,
    model TEXT,
    year INTEGER
    )
    """)
def add_car(conn, name, model, year):
    conn.execute("""
    INSERT INTO car
    VALUES (?, ?, ?)
    """, (name, model, year)
    )
    conn.commit()
# def create_table(conn):
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS student (
#     name TEXT,
#     year INTEGER,
#     last_name
#     )
#     """)
# def add_student(conn, name, year, last_name):
#     conn.execute("""
#     INSERT INTO student
#     VALUES (?, ?, ?)
#     """, (name, year, last_name)
#     )
#     conn.commit()
if __name__ == '__main__':
    connection = sqlite3.connect('database2.py')
    create_tables(connection)
    add_car(connection, "Eldar", "kamri", 2024)
    add_car(connection, "Ilimbek", "mers", 2025)
    add_car(connection, "ali", "tayota", 2022)
    add_car(connection, "beka", "lend gruzer", 2023)
    add_car(connection, "maks", "bugati", 2024)
    add_car(connection, "nurss", "mers1", 2025)
    add_car(connection, "begish", "mers2", 2021)
    add_car(connection, "farux", "mers3", 2018)
    add_car(connection, "jumali", "bmv5", 2021)
    add_car(connection, "alicho", "mers4", 2019)
    # add_student(connection, "Eldar", 2008, "kalmurzaev")
    # add_student(connection, "Ilimbek", 2008, "isaev")
    connection.close()
