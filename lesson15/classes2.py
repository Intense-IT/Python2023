# Создание объектов с уникальными значениями атрибутов


# type() позволяет узнать тип данных объекта
# print(type(1))
# print(type(1.5))
# print(type('asdf'))
# print(type([]))
# print(type(lambda x: x))


class Car:
    # магический метод __init__, вызываемый автоматически
    # в момент создания объекта - позволяет задавать значения
    # свойста в момент создания
    def __init__(self, color, gasoline, spend=3):
        self.speed = 0
        self.gasoline = gasoline
        self.motor = False
        self.color = color
        self.spend = spend

    def start_car(self):  # метод класса
        self.motor = True
        self.speed = 50
        self.gasoline -= self.spend
        print('Ррррр')

    def gasoline_info(self):  # метод класса
        print(f'В баке осталось {self.gasoline} литров')


# Создаем три объекта - экземпляра класса Car
car1 = Car('white', 30, 5)  # позиционные аргументы
car2 = Car('red', 40)
car3 = Car(spend=7, color='blue', gasoline=45)  # именованные аргументы

# Свойства каждого объекта привязаны только к самому объекту
print(car1.color, car1.gasoline, car1.spend)
print(car2.color, car2.gasoline, car2.spend)
print(car3.color, car3.gasoline, car3.spend)

# Но все они относятся к одному классу
print(type(car1))
print(type(car2))
print(type(car3))
