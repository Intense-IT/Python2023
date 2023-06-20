# Программа для готовки блюда из ингредиентов

import random


ACTIONS = ['варим', 'жарим', 'парим', 'запекаем']  # константа действий


# def cook(*args, sauce='аджика'):  # перечень продуктов и соус как значение по умолчанию
def cook(*args, **kwargs):  # перечень продуктов и соус через **kwargs
    # print(args)  # вывели кортеж
    # print(kwargs)  # вывели словарь
    for product in args:
        print(f'{random.choice(ACTIONS)} {product}')
    # print(f'Всё смешаем и заправим {sauce}')
    print(f'Всё смешаем и заправим {kwargs.get("sauce", "аджика")}')
# get() - метод словаря, безопасно возвращающий значение по ключу ("sauce")
# если ключ не найден, вернется значение по умолчанию ("аджика")

cook('лук', 'картофель', 'помидоры', 'мясо', 'сыр', sauce='майонез')
cook('лук', 'картофель', 'помидоры', 'мясо', 'сыр')