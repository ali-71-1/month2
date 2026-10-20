import sqlite3

def create_table(db_name="library.db"):
    """Создает таблицу books в базе данных SQLite."""
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)
    connection.commit()
    connection.close()

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies, db_name="library.db"):
    """Добавляет одну книгу в таблицу books."""
    connection = sqlite3.connect(db_name)
    connection.execute("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, author, publication_year, genre, number_of_pages, number_of_copies))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    # 1. Создаем таблицу
    create_table()

    # 2. Вызываем insert_books 10 раз для разных книг
    insert_books("Война и мир", "Лев Толстой", 1869, "Роман", 1225, 5)
    insert_books("Преступление и наказание", "Фёдор Достоевский", 1866, "Роман", 671, 8)
    insert_books("Мастер и Маргарита", "Михаил Булгаков", 1967, "Фантастика / Роман", 480, 10)
    insert_books("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 6)
    insert_books("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 12)
    insert_books("Отцы и дети", "Иван Тургенев", 1862, "Роман", 288, 4)
    insert_books("Собачье сердце", "Михаил Булгаков", 1925, "Повесть", 160, 7)
    insert_books("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 224, 5)
    insert_books("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Антиутопия", 256, 9)
    insert_books("Граф Монте-Кристо", "Александр Дюма", 1844, "Приключенческий роман", 1248, 3)

    print("Таблица создана, 10 книг успешно добавлены!")