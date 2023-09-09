import requests


# Get-запрос к серверу
# response = requests.get('http://127.0.0.1:8000')
# Явно укажем кодировку, для нормального отображения текста
# response.encoding = 'utf-8'
# print(response.text)


# Множественные get-запросы к серверу
# response = requests.get('http://127.0.0.1:8000')
# while response.text != '0':
#     response = requests.get('http://127.0.0.1:8000')
#     print(response.text)


# Напишем Post-запрос к серверу
# Переменная, хранящая передаваемые в post-запросе данные
my_data = {
    'name': 'Saeed',
    'surname': 'Amirov'
}
# Код самого post-запроса
response = requests.post('http://127.0.0.1:8000', data=my_data)
response.encoding = 'utf-8'
print(response.text)
