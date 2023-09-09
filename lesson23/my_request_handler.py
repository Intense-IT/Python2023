# Импортируем модуль server библиотеки http
import http.server
import random
import sqlite3


# Создаем свой класс обработчика запросов
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Напишем свой метод обработки get-запросов
    def do_GET(self):
        # Отправляем заголовки ответа
        # Указываем код статуса ответа
        self.send_response(200)
        # Указываем, какого типа информация отправляется в ответ
        self.send_header("Content-type", "text/html")
        # Завершаем описание заголовка ответа
        self.end_headers()
        # Данные для ответа записываются методом write переменной wfile
        # self.wfile.write("Here is the answer.".encode('utf-8'))

        # Запишем в качестве ответа HTML-код сайта
        # self.wfile.write("""
        #     <!-- Простой html-сайт -->
        #     <!DOCTYPE html>
        #     <html lang="en">
        #     <head>
        #         <meta charset="UTF-8">
        #         <meta name="viewport" content="width=device-width,
        #                  initial-scale=1.0">
        #         <link rel="stylesheet" href="css/style.css">
        #         <title>Document</title>
        #     </head>
        #     <body>
        #         <h1>Сайт загружен!!</h1>
        #     </body>
        #     </html>
        # """.encode('utf-8'))

        # Вернем в качестве ответа рандомное число
        self.wfile.write(f'{random.randint(0, 3)}'.encode('utf-8'))

    # Напишем свой метод обработки post-запросов
    def do_POST(self):
        # Отправляем заголовки ответа
        # Указываем код статуса ответа
        self.send_response(200)
        # Указываем, какого типа информация отправляется в ответ
        self.send_header("Content-type", "text/html")
        # Завершаем описание заголовка ответа
        self.end_headers()

        # # Можем сразу выслать ответ на запрос.
        # self.wfile.write('Post-запрос получен.'.encode('utf-8'))

        # При считывании необходимо явно указать, сколько данных мы считываем.
        # Иначе процесс повиснет, и результат никогда не будет отправлен.
        # Считываем количество символов из заголовка headers
        content_length = int(self.headers["Content-Length"])
        # Считаем данные и сразу декодируем из байтовой формы
        response = self.rfile.read(content_length).decode()
        # print(response)

        # Обработаем получаемую строку запроса
        # result - словарь, куда запишем обработанные данные
        result = {}
        # Разобьем строку по знаку & и переберем пары
        for pair in response.split('&'):
            # Каждую пару отдельно разобьем на ключ и значение
            data_key, data_value = pair.split('=')
            # Запишем все пары в словарь result как ключ и значение
            result[data_key] = data_value

        # Создаем подключение к БД для внесения данных
        con = sqlite3.connect('lesson23/my_db.db')
        cursor = con.cursor()
        # Создаем БД, если еще не создана
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20),
            surname VARCHAR(20)
        )
        """)
        # Полученные данные запишем в базу данных
        query = "INSERT INTO users(name, surname) VALUES(?, ?)"
        query_data = (result['name'], result['surname'])
        cursor.execute(query, query_data)
        # Подтверждаем изменения в БД
        con.commit()
        # Завершаем работу БД
        cursor.close()
        con.close()

        # Вышлем ответ, что запрос получен
        self.wfile.write('Post-запрос получен.'.encode('utf-8'))


# Метод, создающий и запускающий сервер с нашим обработчиком запросов
def run(server_class=http.server.HTTPServer,
        handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# Выполняем метод для старта сервера
run()
