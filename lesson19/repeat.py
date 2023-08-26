import sqlite3


# создаем соединение с БД и курсор
con = sqlite3.connect('lesson19/first_db.db')
cursor = con.cursor()


# создаем таблицу books
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    author VARCHAR(60),
    year INTEGER(5)
);
""")

# Добавляем запись в таблицу books

# Неэффективый способ добавления записи
# cursor.execute("""
# INSERT INTO books(title, author, year) VALUES (
#     'Маленький принц',
#     'Антуан Экзюпери',
#     1942
# );
# """)

# Эффективный способ добавления записи
# Текст запроса и данные вынесены в отдельные переменные
query = """
INSERT INTO books(title, author, year) VALUES (?, ?, ?)
"""
query_data = ('Маленький принц', 'Антуан Экзюпери', 1942)
cursor.execute(query, query_data)


# Подтверждаем изменения, закрываем курсор и подключение к БД
con.commit()
cursor.close()
con.close()
