# import sqlite3
#
#
# def create_tables(conn):
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS student (
#     name TEXT,
#     age INTEGER,
#     city TEXT
#     )
#     """)
#
#
# def add_student(conn, name, age, city):
#     conn.execute("""
#     INSERT INTO student
#     VALUES (?, ?, ?)
#     """, (name, age, city)
#                  )
#     conn.commit()
#
#
# def create_table(conn):
#     conn.execute("""
#     CREATE TABLE IF NOT EXISTS car (
#     name TEXT,
#     model TEXT,
#     year INTEGER
#     )
#     """)
#     conn.commit()
#
#
# def add_car(conn: object, name: object, model: object, year: object) -> None:
#     """
#
#     :rtype: None
#     """
#     conn.execute("""
#     INSERT INTO car
#     VALUES (?, ?, ?)
#     """, (name, model, year)
#                  )
#     conn.commit()
#
#
# if __name__ == '__main__':
#     connection = sqlite3.connect('database2.db')
#     create_tables(connection)
#     add_student(connection, "Arzybek", 26, "Sokuluk")
#     add_student(connection, "Ali", 18, "Osh")
#     add_student(connection, "Maksat", 17, "Moscow")
#     add_student(connection, "Beka", 17, "Jalal_Abad")
#     add_student(connection, "Nurss", 18, "Osh")
#     add_student(connection, "Eldar", 18, "Osh")
#     add_student(connection, "Ilimbek", 18, "karakol")
#     add_car(connection, "ali", "BMV M5 F90", 2024)
#     add_car(connection, "malsat", "Bugati", 2025)
#     add_car(connection, "zalkar", "mers", 2023)
#     add_car(connection, "beka", "tayota", 2024)
#     add_car(connection, "nurss", "BMV M8", 2025)
#     connection.close()
