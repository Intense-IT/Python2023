# Реляционные базы данных
# Внешний ключ - инструмент связывания двух таблиц БД
import sqlite3


con = sqlite3.connect('lesson20/db_second.db')
cursor = con.cursor()


# Предварительно удаляем таблицы, чтоб записи не накапливались
# в них
cursor.execute("DROP TABLE books")
cursor.execute("DROP TABLE authors")

# Создаем таблицу книг
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    author_id INTEGER,
    year INTEGER(5),
    -- Строка ниже описывает, какое поле - внешний ключ,
    -- и что он указывает (другая таблица, ее поле)
    FOREIGN KEY(author_id) REFERENCES authors(id)
);
""")

# Создаем таблицу авторов
cursor.execute("""
CREATE TABLE IF NOT EXISTS authors(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(60)
);
""")

# Добавление нескольких записей в таблицу authors
author_query = "INSERT INTO authors(name) VALUES(?)"
author_data = [
    ('Лев Толстой',),
    ('Пушкин А. С.',),
    ('Берроуз',)
]
cursor.executemany(author_query, author_data)

# Добавление нескольких записей в таблицу books
books_query = """
INSERT INTO books(title, author_id, year)
VALUES(?, ?, ?)
"""
books_data = [
    ('Война и мир', 1, 1950),
    ('Джанки', 3, 1997),
    ('Анна Каренина', 1, 1877),
    ('Колобок', None, 1000)
]
cursor.executemany(books_query, books_data)

# Получаем данные из двух таблиц
cursor.execute("""
SELECT books.title, authors.name
FROM books, authors
WHERE books.author_id = authors.id
""")
print(cursor.fetchall())


con.commit()
cursor.close()
con.close()
