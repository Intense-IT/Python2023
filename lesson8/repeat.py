num = int(input('Введите число: '))

if num > 0 and num != 20:
    print('Это положительное число, неравное 20.')
elif num == 0:
    print('Это ноль.')
else:
    print('Это отрицательное число.')
    if num == -1: # условие, вложенное в другое условие
        print('Оно равно -1.')
    else:
        print('Оно не равно -1.')