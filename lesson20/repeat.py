import sqlite3


con = sqlite3.connect('lesson20/db_first.db')
cursor = con.cursor()


# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    author VARCHAR(60),
    year INTEGER(5)
);
""")

# Чтение записей
cursor.execute("SELECT * FROM books")
# Вывод данных из курсора в консоль
print(cursor.fetchall())

# Добавление записи
query = "INSERT INTO books(title, author, year) VALUES (?, ?, ?)"
query_data = ('Война и мир', 'Лев Толстой', 1950)
cursor.execute(query, query_data)

# Изменение записей
cursor.execute("""
UPDATE books
SET year = 1869
WHERE title = 'Война и мир'
""")

cursor.execute("SELECT * FROM books")
print(cursor.fetchall())

# Удаление записей
cursor.execute("DELETE FROM books WHERE title = 'Война и мир'")


con.commit()
cursor.close()
con.close()
