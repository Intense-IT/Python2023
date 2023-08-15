# Игра Гонки
# Реализуем двумя путями - через словари и функции и через ООП

from time import sleep


# гоночная трасса
RACE_TRACK = 50


# # функция обычной езды
# def drive(car):
#     car['distance'] += car['speed']
#     car['tank'] -= car['spend']


# # функция включения нитро
# def push_nitro(car):
#     car['distance'] += car['speed'] + car['nitro']
#     car['tank'] -= car['spend'] + car['nitro'] * 1.5


# # функция вывода информации о гонщике
# def racer_info(car):
#     print(f'{car["name"]} проехал {car["distance"]} из {RACE_TRACK}.')
#     print(f'Осталось {car["tank"]} литров топлива.\n')


# # функция выбора игроком действия
# def action(car):
#     your_choice = input(
#         f'{car["name"]}, выберите действие:\n'
#         '1 - обычная езда,\n'
#         '2 - включить нитро.\n'
#         'Ваш выбор: '
#     )
#     if your_choice == 1:
#         drive(car)
#         racer_info(car)
#     else:
#         push_nitro(car)
#         racer_info(car)


# # игрок 1
# car1 = {
#     'name': 'Магомед',
#     'speed': 8,
#     'spend': 4,
#     'tank': 40,
#     'nitro': 4,
#     'distance': 0
# }

# # игрок 2
# car2 = {
#     'name': 'Патимат',
#     'speed': 7,
#     'spend': 3,
#     'tank': 35,
#     'nitro': 5,
#     'distance': 0
# }


# весь игровой процесс
# while True:
#     action(car1)
#     sleep(2)
#     action(car2)
#     sleep(3)


# Класс авто
class Car:
    # конструктор класса Car
    def __init__(self, name, speed, spend, tank, nitro, distance):
        self.name = name
        self.speed = speed
        self.spend = spend
        self.tank = tank
        self.nitro = nitro
        self.distance = distance

    # метод обычной езды класса Car
    def drive(self):
        # этот код
        self.distance += self.speed  # изменяем значение свойства объекта
        self.tank -= self.spend
        # вместо строчек ниже
        # car['distance'] += car['speed']
        # car['tank'] -= car['spend']

    # метод включения нитро
    def push_nitro(self):
        self.distance += self.speed + self.nitro
        self.tank -= self.spend + self.nitro * 1.5

    # метод вывода информации о гонщике
    def racer_info(self):
        print(f'{self.name} проехал {self.distance} из {RACE_TRACK}.')
        print(f'Осталось {self.tank} литров топлива.\n')

    # метод выбора игроком действия
    def action(self):
        your_choice = input(
            f'{self.name}, выберите действие:\n'
            '1 - обычная езда,\n'
            '2 - включить нитро.\n'
            'Ваш выбор: '
        )
        if your_choice == 1:
            self.drive()
            self.racer_info()
        else:
            self.push_nitro()
            self.racer_info()

    # метод проверки на победу и проигрыш
    def win_or_lose(self):
        if self.distance >= RACE_TRACK:
            print(f'{self.name} победил!')
            return True
        elif self.tank <= 0:
            print(f'{self.name} проиграл!')
            return True
        return False


# вся исполняемая часть кода обернута в ф-ию main()
def main():
    car1 = Car('Магомед', 8, 4, 45, 4, 0)
    car2 = Car('Патимат', 7, 3, 40, 5, 0)

    while True:
        car1.action()
        sleep(2)
        car2.action()
        sleep(2)
        if car1.win_or_lose() or car2.win_or_lose():
            break


# ф-ия main выполняется только если это исполняемый файл
if __name__ == '__main__':
    main()
