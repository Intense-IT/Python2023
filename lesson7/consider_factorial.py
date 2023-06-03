# Программа на проверку навыка вычисления факториала

import math
import random


random_num = random.randint(0, 10) # получаем случайное значение для факториала
result = int(input('Факториал числа ' + str(random_num) + ' равен: '))
if result == math.factorial(random_num): # сверяем информацию от пользователя с вычисленным
    print('Ответ верный!')
else:
    print('Неверно! Учи математику!')
