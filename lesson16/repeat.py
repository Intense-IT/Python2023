# Класс - тип данных
# Объект - экземпляр класса

class Car:
    # __init__() - магический метод, конструктор класса
    def __init__(self, wheels):  # self хранит ссылку на объект
        self.wheels = wheels  # свойство/атрибут класса

    def ride(self):  # метод класса Car
        print('Вррррр')


my_car = Car(3)  # экземпляр класса Car
print(my_car)  # выводим сам объект
print(my_car.wheels)  # выводим значение свойства wheels объекта my_car
my_car.ride()  # вызываем метод ride класса Car к объекту my_car
