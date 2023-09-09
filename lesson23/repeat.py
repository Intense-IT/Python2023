# Импортируем модуль server библиотеки http
import http.server


# Метод, создающий и запускающий сервер
def run(server_class=http.server.HTTPServer,
        handler_class=http.server.SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# Выполняем метод для старта сервера
run()
