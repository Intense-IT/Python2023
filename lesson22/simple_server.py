# Библиотека http, содержащая модули для работы с http
# https://docs.python.org/3/library/http.html

import http.server


# http.HTTPStatus.OK и т.д. - константы кода статуса
# http.HTTPMethod.GET и т.д. - константы методов запроса

# Создаем экземпляр сервера и записываем в переменную httpd
# httpd = http.server.HTTPServer(
#     ('', 8000),
#     http.server.SimpleHTTPRequestHandler
# )

# Занесем создание сервера в функцию run()
# В качестве именованных аргументов передаются
# класс сервера и класс обработчика запросов
# В данном случае обработчик запросов - SimpleHTTPRequestHandler
# def run(server_class=http.server.HTTPServer,
#         handler_class=http.server.SimpleHTTPRequestHandler):
#     server_address = ('', 8000)
#     httpd = server_class(server_address, handler_class)
#     httpd.serve_forever()


# В данном случае обработчик запросов - CGIHTTPRequestHandler
# Исполняемый файл в папке cgi-bin выводит в консоль информацию,
# которая и будет отправлена в форме ответа на запрос
# https://ru.wikipedia.org/wiki/CGI
def run(server_class=http.server.HTTPServer,
        handler_class=http.server.CGIHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


run()
