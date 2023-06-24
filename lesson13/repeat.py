def simple_func(*args, **kwargs):
    print(args)  # кортеж
    print(kwargs)  # словарь

# simple_func(1, 2, 3, x='qwerty', y='йцукен')

num_list = [1, 2, 3, 4]
print(list(filter(lambda x: x > 2, num_list)))  # отфильтруем набор данных по условию
print(list(map(lambda x: x ** 2, num_list)))  # возведем все элементы списка в степень