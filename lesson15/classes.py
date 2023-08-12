# ООП - объектно-ориентированное программирование
# Классы и объекты
# Класс - тип данных
# Объект - экземпляр класса

# ПРОЦЕДУРНОЕ ПРОГРАММИРОВАНИЕ
# def start_car():
#     global motor1, speed1, gasoline1
#     motor1 = True
#     speed1 = 50
#     gasoline1 -= 3

# speed1 = 0
# gasoline1 = 20
# motor1 = False

# start_car()
# print(speed1, gasoline1, motor1)


# ---------------------------------------

# ПРОЦЕДУРНОЕ ПРОГРАММИРОВАНИЕ С АБСТРАКЦИЯМИ
# Создаем общий метод
# def start_car(car):
#     car['motor'] = True
#     car['speed'] = 50
#     car['gasoline'] -= car['spend']


# # Создаем два автомобиля посредством словарей
# car1 = {
#     'speed': 0,
#     'gasoline': 20,
#     'motor': False,
#     'color': 'white',
#     'spend': 3
# }
# car2 = {
#     'speed': 0,
#     'gasoline': 40,
#     'motor': False,
#     'color': 'red',
#     'spend': 5
# }


# # Вызываем метод для каждого словаря
# start_car(car1)
# start_car(car2)
# print(car1)
# print(car2)


# ---------------------------------------

# ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ
class Car:  # class - зарезервированное слово, Car - имя класса
    speed = 0  # свойство/атрибут класса Car
    gasoline = 20
    motor = False
    color = 'white'
    spend = 3

    def start_car(self):  # метод класса Car
        # self хранит ссылку на конкретный объект, у которого вызываются методы
        # и изменяются свойства
        self.motor = True
        self.speed = 50
        self.gasoline -= self.spend
        print('Ррррр')

    def gasoline_info(self):  # метод класса Car
        print(f'В баке осталось {self.gasoline} литров')


car1 = Car()  # создаем экземпляр класса Car
car1.gasoline_info()  # вызываем метод проверки уровня бензина
car1.start_car()  # заводим авто
car1.gasoline_info()
print(car1.gasoline)
print(car1)
car2 = Car()
print(car2.gasoline)  # свойства car2 не зависят от car1
# объекту можно добавить новое свойство
car2.breaks = 'сдулось колесо'
print(car2.breaks)
