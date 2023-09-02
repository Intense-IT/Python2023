# Программа, делающая запросы к сервису Геокодер API Яндекс.Карт
# Ссылка на документацию Геокодер API Яндекс.Карт
# https://yandex.ru/dev/geocode/doc/ru/
import requests

# Адрес сервиса, куда делается запрос
geo_api_server = 'http://geocode-maps.yandex.ru/1.x/'
# Передаваемые параметры, среди которых ключ API
geo_params = {
    'apikey': '39e26183-aaa8-4978-b294-d0b902ced272',
    'geocode': 'Махачкала',
    'format': 'json'
}
response = requests.get(geo_api_server, params=geo_params)
# Полученный результат необходимо преобразовать из JSON
json_response = response.json()

# В результате мы получаем словарь с большим количеством данных
# Далее мы с этими данными работаем
toponym = json_response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']

print(toponym['metaDataProperty']['GeocoderMetaData']['text'])
print(toponym['Point']['pos'])
