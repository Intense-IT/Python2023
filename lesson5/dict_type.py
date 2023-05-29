# Словарь - неупорядоченный изменяемый тип данных
# Информация хранится в виде пар "ключ: значение"

# Создание словаря
# it_dict = {}
it_dict = {'переменная': 'инструмент хранения данных', 
           'dns': 'доменное имя', 5: 'целое число',
           False: 'логический тип',
           ('огурцы', 'помидоры'): 'овощи'}
print(it_dict)

# Добавление записи
it_dict['база данных'] = 'табличный способ хранения данных'
print(it_dict)

# Получение значения по ключу
print(it_dict[('огурцы', 'помидоры')]) 
print(it_dict[False])

# Изменение значения
it_dict['база данных'] = 'Совокупность данных' 
print(it_dict)

# Удаление записи
del it_dict['база данных']
print(it_dict)

del it_dict # удаление словаря