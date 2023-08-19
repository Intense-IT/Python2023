# Магические методы

# Магический метод __init__ вызывается при создании экземпляра класса

# Магические методы __str__ и __repr__

class Cat():
    def __init__(self, name):
        self.name = name
        self.age = 3
        self.weight = 10

    # __str__ - магический метод, отвечающий за отображение информации,
    # хранимой в объекте, при выводе пользователю
    def __str__(self):
        return f'Это кошка по имени {self.name}, весящая {self.weight} кг!'
    # Возвращаемая информация только строкового типа

    # __repr__ - магический метод, отвечающий за отображение информации,
    # хранимой в объекте, при передаче другим стурктурам.
    def __repr__(self):
        return {
            'name': self.name,
            'age': self.age,
            'weight': self.weight
        }
    # Возвращаемая информация может быть любого типа


# Создаем экземпляр класса Cat
my_cat = Cat('Снежок')
# Вызовем метод __str__() у объекта my_cat командой print
print(my_cat)
# Вызовем метод __repr__() у объекта my_cat
print(my_cat.__repr__())


class Bank_account:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # Переопределим магический метод __str__
    def __str__(self):
        return f'На счету {self.name} - {self.money}$'

    # Магические методы для операций сравнения
    # __eq__(self, other) - магический метод для операции " == "
    # __ne__(self, other) - магический метод для операции " != "
    # __lt__(self, other) - магический метод для операции " < "
    # __gt__(self, other) - магический метод для операции " > "
    # __le__(self, other) - магический метод для операции " <= "
    # __ge__(self, other) - магический метод для операции " >= "

    # Для операции x > y вызов метода выглядит так: x.__gt__(y)
    def __gt__(self, other):
        # сравниваем не объекты, а их свойства money
        return self.money > other.money

    # Магические методы для арифметических операций
    # __add__(self, other) - магический метод для операции сложения " + "
    # __sub__(self, other) - магический метод для операции вычитания " - "
    # __mul__(self, other) - магический метод для операции умножения " * "
    # __div__(self, other) - магический метод для операции деления " / "
    # __floordiv__(self, other) - магический метод для операции
    # целочисленного деления " // "

    # Для операции x + y вызов метода выглядит так: x.__add__(y)
    def __add__(self, other):
        return self.money + other.money
        # При желании можно менять значения свойств и вызывать методы
        # self.money = self.money + other.money
        # other.money = 0
        # return self.money


# Создаем экземпляр класса Bank_account
my_account = Bank_account('Саид', 10000)
# При выводе значения объекта сработает магический метод __str__
print(my_account)

neighbor_acc = Bank_account('Магомед', 5000)

# При сравнении объектов сработает магический метод __gt__
if my_account > neighbor_acc:
    print('Я победил!')
else:
    print('Победил сосед ;(')

# При сложении объектов сработает магический метод __add__
print(my_account + neighbor_acc)
