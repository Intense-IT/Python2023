# База данных - это набор информации, организованно хранящийся
# в электронном виде.

# Реляционная база данных -  база данных,
# основанная на реляционной модели данных
# («реляционный» подразумевает математическое понятие «отношение»,
# «relation» - взаимосвязь различных объектов).

# СУБД (система управления базами данных) - комплекс программ,
# позволяющих управлять базой данных, ее таблицами и
# манипулировать хранящимися в них данными.

# SQL (Structured Query Language) - декларативный язык программирования,
# применяемый для управления данными в реляционной базе данных.

# Библиотека для SQLite является базовой в Python
import sqlite3


con = sqlite3.connect('lesson18/new.db')  # подключаемся к БД
cursor = con.cursor()  # создаем курсор/каретка/бегунок


# Команда DROP TABLE удаляет таблицу
cursor.execute('''
DROP TABLE books;
''')

# execute() - метод, выполняющий SQL-запросы.
# Этому методы передается SQL-запрос в виде многострочного объекта.
cursor.execute('''
-- Двойное тире это знак однострочного комментария в SQL

-- CREATE TABLE books (
-- Команда CREATE TABLE IF NOT EXISTS создает таблицу,
-- только если ее до этого не существовало

CREATE TABLE IF NOT EXISTS books (
    -- UNIQUE говорит, что поле должно быть уникальным
    -- id INTEGER UNIQUE,
    -- PRIMARY KEY говорит, что данное поле - первичный ключ
    -- AUTOINCREMENT - значение выдается автоматом, увеличивая предыдущее на 1

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    author VARCHAR(50),
    year INTEGER(5)
);
''')

# Добавим в таблицу books запись
cursor.execute('''
-- Команда INSERT INTO вставляет запись в указанную таблицу
INSERT INTO books VALUES (
    1,
    'Оно',
    'Стивен Кинг',
    1986
);
''')

# Добавим запись с полями title, author, year, т.е. без id,
# т.к. id выдается автоматически
cursor.execute('''
INSERT INTO books(title, author, year) VALUES (
    'Бойцовский клуб',
    'Чак Паланик',
    1996
);
''')

# Добавим запись без поля year.
# В качестве значения в ячейку запишется null
cursor.execute('''
INSERT INTO books(title, author) VALUES (
    'Крестный отец',
    'Марио Пьюзо'
);
''')

# Неэффективный путь добавления данных в запрос
# Данные для SQL-запроса
# query_data = ('Собачье сердце', 'Михаил Булгаков', 1925)
# full_query = f'''
# INSERT INTO books(title, author, year) VALUES (
#     '{query_data[0]}',
#     '{query_data[1]}',
#     {query_data[2]}
# );
# '''
# cursor.execute(full_query)

# Ниже более эффективный путь добавления данных в запрос
# query_data = ('Собачье сердце', 'Михаил Булгаков', 1925)
# cursor.execute(
#     '''INSERT INTO books(title, author, year) VALUES(?, ?, ?)''',
#     query_data)

# Самый эффективный путь добавления данных в запрос.
# Сам запрос и данные вынесены в отдельные переменные.
query_data = ('Собачье сердце', 'Михаил Булгаков', 1925)
query = '''INSERT INTO books(title, author, year) VALUES(?, ?, ?)'''
cursor.execute(query, query_data)

con.commit()  # подтверждаем все изменения, внесенные в БД
cursor.close()  # закрываем курсор
con.close()  # закрываем соединение с БД
