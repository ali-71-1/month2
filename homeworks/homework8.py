import sqlite3

def create_table(db_name="library.db"):
    """Создаёт таблицу books, если она ещё не существует."""
    with sqlite3.connect(db_name) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                author TEXT NOT NULL,
                publication_year INTEGER,
                genre TEXT,
                number_of_pages INTEGER,
                number_of_copies INTEGER
            )
        """)
        connection.commit()

def insert_books(name: str, author: str, publication_year: int, genre: str, number_of_pages: int, number_of_copies: int, db_name="library.db"):
    """Добавляет одну книгу в таблицу books."""
    with sqlite3.connect(db_name) as connection:
        connection.execute("""
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, author, publication_year, genre, number_of_pages, number_of_copies))
        connection.commit()

def get_books_by_author(author: str, db_name="library.db"):
    """Возвращает список всех книг указанного автора."""
    with sqlite3.connect(db_name) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT * FROM books WHERE author = ?
        """, (author,))
        books = cursor.fetchall()
        return books

def delete_book_by_id(book_id: int, db_name="library.db"):
    """Удаляет книгу из таблицы books по её уникальному идентификатору (ID)."""
    with sqlite3.connect(db_name) as connection:
        connection.execute("""
            DELETE FROM books WHERE id = ?
        """, (book_id,))
        connection.commit()
        print(f"Книга с ID {book_id} успешно удалена.")

if __name__ == "__main__":
    # 1. Создаём таблицу
    create_table()

    # 2. Вызываем функцию insert_books 10 раз для каждой книги отдельно
    insert_books("Война и мир", "Лев Толстой", 1869, "Роман-эпопея", 1225, 5)
    insert_books("Преступление и наказание", "Фёдор Достоевский", 1866, "Психологический роман", 671, 3)
    insert_books("Мастер и Маргарита", "Михаил Булгаков", 1967, "Мистика, Роман", 480, 7)
    insert_books("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 10)
    insert_books("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 4)
    insert_books("Анна Каренина", "Лев Толстой", 1877, "Роман", 864, 2)
    insert_books("Отцы и дети", "Иван Тургенев", 1862, "Роман", 288, 6)
    insert_books("Герой нашего времени", "Михаил Лермонтов", 1840, "Роман", 224, 8)
    insert_books("451° по Фаренгейту", "Рэй Брэдбери", 1953, "Антиутопия", 256, 5)
    insert_books("Собачье сердце", "Михаил Булгаков", 1925, "Повесть", 160, 4)

    print("Таблица создана, 10 книг добавлены в базу данных!\n")

    # 3. Демонстрация работы get_books_by_author
    search_author = "Лев Толстой"
    print(f"Поиск книг автора: {search_author}")
    author_books = get_books_by_author(search_author)
    for book in author_books:
        print(book)
    print()

    # 4. Демонстрация работы delete_book_by_id (например, удалим книгу с ID 10)
    print("Удаляем книгу с ID 10...")
    delete_book_by_id(10)