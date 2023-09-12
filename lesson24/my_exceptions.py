# Создаем свой тип исключений
class BirthYearError(Exception):
    # Опишем, что возвращается при получении
    # строкового значения объекта
    def __str__(self):
        return 'Введен невозможный год рождения.'


try:
    year = int(input('Введите ваш год рождения: '))
    if year < 1900 or year > 2023:
        # Мы сами поднимаем исключение при определенном условии
        # Тип ошибок ValueError не соответствует поднимаемому исключению
        # raise ValueError
        # Вместо этого поднимем ошибку созданного нами типа
        raise BirthYearError
    print(f'Значение {year} принято, вы зарегистрированы.')
except ValueError:
    print('Введено значение несоответствующего типа.')
# Проводим отлов написанного нами исключения среди прочих
except BirthYearError as error:
    print('Error:', error)
except Exception as error:
    print('Error:', error)


# Рассмотрим пути обработки исключения
num1 = int(input())
num2 = int(input())

# Первый подход в разработке
# Все проверки до основного блока кода
# Look Before You Leap - LBYL
# "Посмотри перед прыжком"
if num2 == 0:
    print('У вас ошибка - на ноль делить нельзя!')
else:
    print(num1 / num2)

# Второй подход
# Ошибки отлавливаются по ходу исполнения основного блока кода
# Easier to Ask Forgiveness than Permission - EAFP
# "Проще попросить прощения, чем разрешения"
try:
    print(num1 / num2)
except ZeroDivisionError as error:
    print('На ноль делить нельзя!', error)
