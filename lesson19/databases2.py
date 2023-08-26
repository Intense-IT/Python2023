# Рассматриваем считывание данных из таблицы БД
import sqlite3


# Создаем соединение с БД и курсор
con = sqlite3.connect('lesson19/second_db.db')
cursor = con.cursor()


# Создаем таблицу books
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    author VARCHAR(60),
    year INTEGER(5)
);
""")

# Добавим 5 записей в таблицу через команду executemany
query = """
INSERT INTO books(title, author, year) VALUES (?, ?, ?);
"""
books_list = [
    ('Властелин колец', 'Джон Толкин', 1949),
    ('Зеленая миля', 'Стивен Кинг', 1996),
    ('Финансист', 'Теодор Драйзер', 1912),
    ('Титан', 'Теодор Драйзер', 1914),
    ('Стоик', 'Теодор Драйзер', 1945)
]
# cursor.executemany(query, books_list)

# Считывание данных из таблицы
# Для этого применяется конструкция SELECT ... FROM ...
cursor.execute("""SELECT * FROM books""")
cursor.execute("""SELECT title FROM books""")
cursor.execute("""SELECT title, year FROM books""")
# Можно прописывать условия проверки
cursor.execute("""SELECT title, year FROM books WHERE year < 1940""")
cursor.execute("""SELECT title, year FROM books WHERE year = 1945""")
# Можно применять логические операторы OR, AND, NOT
cursor.execute("""
SELECT title, year
FROM books
WHERE year > 1930 AND year < 1950 ORDER BY year DESC LIMIT 1
""")
# BETWEEN ... AND ... - команда проверки вхождения в интервал
cursor.execute("""
SELECT title, year
FROM books
WHERE year BETWEEN 1930 AND 1950
""")
# IN позволяет проверить вхождение значения в список
cursor.execute("""
SELECT title, year
FROM books
WHERE author IN ('Чак Паланик', 'Теодор Драйзер', 'Виктор Пелевин')
""")
# Команда LIKE принимает шаблон строки
# со знаками % (ноль, один или неск. символов) и _ (один символ)
cursor.execute("""
SELECT title, year
FROM books
WHERE title LIKE '% колец'
""")

# Команда fetchall() возвращает данные из курсора
# print(cursor.fetchall())

# По курсору можно пройтись как по итератору циклом
# for row in cursor:
#     print(row)

# GROUP BY позволяет сгруппировать записи по полям
# Можно вызывать функции SQL для группы данных: MIN, MAX, AVG, SUM, COUNT
cursor.execute("""
SELECT author, COUNT()
FROM books
GROUP BY author
""")
print(cursor.fetchall())


# Изменение данных командой UPDATE ... SET ... WHERE ...
cursor.execute("""
UPDATE books
SET author = 'С. Кинг'
WHERE author = 'Стивен Кинг'
""")


# Удаление данных командой DELETE ... WHERE ...
cursor.execute("""
DELETE FROM books
WHERE author = 'С. Кинг'
""")

# Посмотрим результат
cursor.execute("""SELECT * FROM books""")
print(cursor.fetchall())

con.commit()
cursor.close()
con.close()
