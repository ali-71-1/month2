import sqlite3
def create_tables(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT,
        year INTEGER
        )
    ''')
def add_student(conn, name, age, city, year):
    conn.execute('''
        INSERT INTO students (name, age, city, year)
        VALUES (?, ?, ?, ?)
    ''', (name, age, city, year)
    )
    conn.commit()

def get_all_students(conn):
    result = conn.execute('''
        SELECT name, id FROM students
    ''').fetchmany(2)
    return result
    # result = conn.execute('''
    #         SELECT name, id FROM students
    #     ''').fetchall()
    # return result

def get_student(conn, student_id):
    result = conn.execute('''
        SELECT * FROM students WHERE id = ?
        ''', (student_id,)
    ).fetchone()
    return result
def get_students_by_age(conn, age):
    result = conn.execute('''
        SELECT * FROM students WHERE age > ?
        ''', (age,)
    ).fetchall()
    return result

def delete_student_by_name(conn, name):
    conn.execute('''
        DELETE FROM students WHERE name = ?
    ''', (name,)
    )
    conn.commit()


def delete_student(conn, student_id):
    conn.execute('''
        DELETE FROM students WHERE id = ?
    ''', (student_id,)
    )
    conn.commit()


if __name__ == '__main__':
    connection = sqlite3.connect('database3.db')
    create_tables(connection)
    add_student(connection, "Eldar", 34, "Osh", 2008)
    add_student(connection, "Ilimbek", 18, "karakol", 2008)
    add_student(connection, "ali", 33, "Osh", 2008)
    delete_student(connection, 2)
    delete_student_by_name(connection, "Ilimbek")
    all_students = get_all_students(connection)
    print(all_students)
    for st in all_students:
        print(st)
    one_student = get_student(connection, 7000)
    print(one_student)
    old_student = get_students_by_age(connection, 30)
    print("старше чем 30:")
    print(old_student)
    connection.close()