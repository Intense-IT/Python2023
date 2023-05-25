# Множество - неповторяющийся неупорядоченный набор данных

films = {"Интерстеллар", "Стражи галактики 3", "Форсаж 20", "Форсаж 20"}
print(films) # вывод множества films
fav_films = {"Воин", "Начало", "Форсаж 20"}

# Операции над множеством
films.add("Банды Нью-Йорка") # add() добавляет элемент в множество
films.discard("Стражи галактики 3") # remove() удаляет элемент из множества, если в наличии

# Операции над двумя множествами
print("Пересечение: ", films & fav_films) 
print("Объединение: ", films | fav_films) 
print("Разность 1: ", films - fav_films) 
print("Разность 2: ", fav_films - films)
