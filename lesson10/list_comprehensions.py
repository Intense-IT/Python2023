# Списочные выражения

# [<выражение> <цикл for>] - упрощенная структура
num_list = [x for x in range(10)] # перебираем в цикле значения x и записываем в список
print(num_list)

num_list2 = [0 for _ in range(100)]  # проходим по итератору и записываем в список значение 0
print(num_list2)

input_list = [int(input()) for _ in range(4)]  # вводим с консоли, преобразуем в int и добавляем
print(input_list)

# [<выражение> <цикл for> <условие>] - списочное выражение с условием if
num_list3 = [x ** 2 for x in input_list if x > 0]  # все непрошедшие проверку условия элементы не добавляются в список
print(num_list3)

# [<выражение> <условие> <выражение> <цикл for>] - списочное выражение с условием if..else
num_list4 = [x ** 2 if x > 0 else x ** 3 for x in input_list]  # в зависимости от условия выполняются разные выражения
print(num_list4)
