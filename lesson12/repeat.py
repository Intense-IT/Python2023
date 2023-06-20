# Именованные и позиционные аргументы, значения по умолчанию

def mult_func(x=1, y=1):  # значения по умолчанию
    return x * y

print(mult_func())  # без аргументов
print(mult_func(y=5, x=2))  # именованные аргументы