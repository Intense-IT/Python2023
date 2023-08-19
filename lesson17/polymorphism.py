# Полиморфизм - принцип ООП

# Класс для создания самолетов
class Airplane:
    weight = 1000000

    def fly(self):  # метод полета самолета
        print('Турбины крутятся жж-ж-ж-жж!')


# Класс для создания птиц
class Bird:
    def fly(self):  # метод полета птицы
        print('Птица машет крыльями.')

    def bird_fly(self):  # этот метод незнаком ф-ии start_fly()
        print('Птица машет крыльями.')


# Ф-ия старта полета
def start_fly(obj):
    obj.fly()


# Создаем объекты по классам
plane = Airplane()
pigeon = Bird()

# вызываем метод start_fly с разными типами объектов без каких-либо ошибок
start_fly(plane)
start_fly(pigeon)
