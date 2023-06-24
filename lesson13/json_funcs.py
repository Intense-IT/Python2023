# Работа с json-файлами

import json

# Чтение с json-файла
with open('lesson13/data.json', encoding='UTF-8') as json_file:
    json_info = json.load(json_file)  # load выгружает и преобразует данные из json в Python-формат

# С полученными данными можно работать как с обычной стуктурой Python
print(json_info)
print(json_info[0]['fio'])
print(json_info[1])

# Словарь с информацией о фильмах
films_info = {
    'genres': ['ужас', 'триллер', 'комедия'],
    'titles': ['It', 'Пила', 'Мачо и ботан']
}

# Запись в json-файл
with open('lesson13/films.json', 'w', encoding='UTF-8') as films_file:
    json.dump(films_info, films_file, ensure_ascii=False, indent=2)
# dump - преобразует данные в json и загружает в файл
# атрибут ensure_ascii нужен для отключения запрета на небезопасные символы типа кириллицы
# indent - добавляет отступы и переносы в json