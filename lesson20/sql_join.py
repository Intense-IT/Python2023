# JOIN - команда для объединения нескольких групп данных
# из разных таблиц
import sqlite3


con = sqlite3.connect('lesson20/db_third.db')
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


# Получим связанный набор данных из нескольких таблиц

# Этот способ просто перебирает все комбинации записей двух таблиц
# cursor.execute("""
# SELECT *
# FROM books, authors
# """)

# Этот способ отсеивает данные двух таблиц, не связанные между собой
cursor.execute("""
SELECT *
FROM books, authors
WHERE books.author_id = authors.id;
""")

# Способ ниже работает таких же образом, однако является
# рекомендованным для подобных задач
# INNER JOIN - в итоговый набор попадают только записи,
# соответствующие условию
cursor.execute("""
SELECT *
FROM books
INNER JOIN authors ON books.author_id = authors.id
""")

# LEFT JOIN - в итоговый набор попадают все записи первой таблицы,
# даже те, которым нет соответствующего значения во второй таблице.
# Отсутствующие значения второй таблицы заменяются на null/None.
cursor.execute("""
SELECT *
FROM books
LEFT JOIN authors ON books.author_id = authors.id
""")

# RIGHT JOIN - работает аналогично LEFT JOIN, но за основу берется
# правая, вторая таблица.
cursor.execute("""
SELECT *
FROM books
RIGHT JOIN authors ON books.author_id = authors.id
""")

# При необходимости можно писать длинные цепочки JOIN
# cursor.execute("""
# SELECT *
# FROM books
# LEFT JOIN authors ON books.author_id = authors.id
# LEFT JOIN reviews ON books.review_id = reviews.id
# """)

print(cursor.fetchall())


con.commit()
cursor.close()
con.close()
