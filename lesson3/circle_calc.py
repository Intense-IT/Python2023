import math


# программа рассчета длины и площади окружности
radius = int(input("Введите радиус окружности: "))
c_length = round(2 * math.pi * radius, 2)
c_square = round(math.pi * radius ** 2, 2)
print("Длина окружности:", c_length)
print("Площадь окружности:", c_square)