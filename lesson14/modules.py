# import vars_and_funcs  # подключим наш файл как библиотеку


# vars_and_funcs.my_func(20)  # вызовем функцию my_func из файла vars_and_funcs.py
# print(vars_and_funcs.my_num)  # выведем значение my_num из файла vars_and_funcs.py


from vars_and_funcs import my_func, my_num  # точечно импортируем функции и переменные

my_func(20)  # используем без указания библиотеки
print(my_num)  # используем без указания библиотеки
