# Команды и методы списков

cities = ['Москва', 'Махачкала', 'Каир', 'Каспийск']

print(len(cities)) # len() - количество элементов в списке
print(cities.index('Каир')) # index() - индекс по значению
print(cities.count('Каспийск')) # count() - количество вхождений

numbers = [5, 23, 4.1, -8]
print(min(cities)) # min() - наименьшее значение списка
print(max(numbers)) # min() - наибольшее значение списка

cities_text = ', '.join(cities) # join() склеивает список в строку
print(cities_text)
print(cities_text.split(', ')) # split() разбивает строку на элементы списка

print(cities.reverse()) # reverse() инвертирует последовательность в списке
print(cities)

# print(cities.sort()) # sort() - сортирует элементы в списке
print(sorted(cities)) # sorted() - возвращает отсортированный список
print(cities)

cities.sort(reverse=True) # сортирует по убыванию
print(cities)
cities.sort(key=lambda x:x[1]) # сортирует по длине элементов списка
print(cities)

# cities_copy = cities # скопировали ссылку
# cities_copy = cities[:] # создали копию списка, способ 1
cities_copy = cities.copy() # создали копию списка, способ 2
cities_copy[0] = "Дербент"
print(cities)
print(cities_copy)

print("Лондон" in cities) # in - проверяет наличие в списке
print("Париж" not in cities) # not in - проверяет отсутсвие в списке
