# Мы можем отправлять запросы к нашему локальному серверу
import requests


response = requests.get('http://127.0.0.1:8000')
print(response.status_code)
print(response.text)
