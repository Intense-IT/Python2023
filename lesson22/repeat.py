import requests


# Сделаем get-запрос
my_params = {
    'id': 12353
}
response = requests.get(
    'https://ru.wikipedia.org/wiki/',
    params=my_params)
print(response.status_code)
print(response.text)
print(response.content)


# Сделаем post-запрос
# Запишем в переменную словарь с данными для post-запроса
post_data = {
    'fio': 'Магомедов М. М.',
    'age': 25
}
response = requests.post(
    'https://ru.wikipedia.org/wiki/',
    data=post_data)
print(response.text)


