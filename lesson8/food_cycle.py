# Управление списком покупок

food_list = []
food_count = 0
while True:  # начало цикла
    food = input('Укажите продукт к покупке: ')
    if food == 'Хватит':
        break  # прерывает выполнение цикла
    food_count += 1
    if food == 'Пропустить':
        continue  # прерывает текущую итерацию цикла
    food_list.append('Покупка №' + str(food_count) + ': ' + food)  # добавление записи в список
print(food_list)
