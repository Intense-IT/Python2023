# def avg_func(num_list):
#     return sum(num_list) / len(num_list)


# print(avg_func([10, 2, 23, 15]))  # передаем список как аргумент

def avg_func(*args):  # *args - хранит все позиционные аргументы в форме кортежа
    return sum(args) / len(args)


print(avg_func(23, 12, 33, 21))  # работает с любым количеством аргументов