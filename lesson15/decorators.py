# Декораторы - инструмент, позволяющий расширять возможности
# функции без изменений ее исходного кода


# Структура декоратора
# def <имя декоратора>(<имя переменной, хранящей исходную ф-ю>)
#     def <имя убертки для функции>(*args, **kwargs):
#         Блок кода с вызовом исходной функции и др. возможностями
#     return <имя обертку>


# Декоратор 1, добавляющий в конец результата "."
def add_mark(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + '.'
    return wrapper


# Декоратор 2, выводящий в консоль информацию о функции
def func_info(func):
    def wrapper(*args, **kwargs):
        print(f'Название функции: {func.__name__}')
        print(f'Позиционные аргументы: {args}')
        print(f'Именованные аргументы: {kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат выполнения функции: {result}')
        return result
    return wrapper


# функция приветствия, которую расширили декоратором add_mark
@add_mark
def greeting(name):
    return f'Hello, {name}'


# ф-ия диалога, расширенная декоратором func_info
@func_info
def dialogue(name):
    return f'How are you, {name}'


# ф-ия прощания, расширенная декораторами func_info и add_mark
@func_info
@add_mark
def goodbye(name):
    return f'Goodbye, {name}'


print(greeting('Саид'))
print(dialogue('Магомед'))
print(goodbye('Патимат'))

# декоратором создается новая ф-ия, которая сохраняется
# в переменную new_greeting
new_greeting = func_info(greeting)
new_greeting('Заур')
