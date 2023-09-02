# Библиотека requests для отправки запросов
# https://requests.readthedocs.io/en/latest/
# Перед импортом необходимо установить библиотеку через терминал
# pip install requests
import requests


# Пример запроса к сайту - осуществляется через метод get()
# В переменную response сохраняется ответ на запрос
response = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart/')

print(response)  # выводим в консоль объект ответа

print(response.status_code)  # выводим статус ответа
# https://ru.wikipedia.org/wiki/Список_кодов_состояния_HTTP

# print(response.content)  # выводим содержимое ответа

# print(response.text)  # выводим содержимое ответа в виде текста

# Документация к Static API Яндекс.Карт
# https://yandex.ru/dev/staticapi/doc/ru/

# Пример запроса к сервису Яндекс.карт
# https://static-maps.yandex.ru/1.x/?ll=47.499175,42.974169&spn=0.005,0.005&l=map
response = requests.get(
    'https://static-maps.yandex.ru/1.x/?ll=47.499175,42.974169&spn=0.005,0.005&l=map')
print(response.content)

# Перепишем код запроса в более эффективную форму
# Отдельная переменная для указания сервиса, куда делается запрос
api_server = 'https://static-maps.yandex.ru/1.x/'
# Отдельная переменная для словаря, хранящего все параметры
map_params = {
    'll': '47.499175,42.974169',
    'spn': '0.005,0.005',
    'l': 'map'
}
# В сам метод get() передаются последовательно обе переменные
response = requests.get(api_server, params=map_params)
print(response)
