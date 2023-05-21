number1 = 20
number2 = "3.5"
# print(number1 + number2) # даст ошибку
print(str(number1) + number2) # str() int -> str
# print(number1 + int(number2)) # int() str -/> int, даст ошибку
print(number1 + float(number2)) #  float() str -> float
print(int(3.5)) # преобразование float -> int