# Работа с текстовыми файлами

my_file = open('lesson13/text_file.txt', encoding='UTF-8')  # устанавливаем соединение с файлом

# full_text = my_file.read()  # считывается весь текст
# print(full_text)

# part_text = my_file.read(30)  # считать текст до 30-го символа
# print(part_text)

for line in my_file:  # последовательно перебираем строки файла
    # print(line)
    # print(line, end='')
    print(line.rstrip('\n'))  # удаляем переводы на новую строку в конце каждой строки

my_file.close()  # закрывает соединение с файлом

# with - менеджер контекста
with open('lesson13/text_file.txt', encoding='UTF-8') as my_file2: 
    part_text = my_file2.read(30)  # считать текст до 30-го символа
print(part_text)

# Для записи откроем с режимом "w" - write, запись с удалением прошлых данных
with open('lesson13/text_file.txt', 'w', encoding='UTF-8') as my_file2:
    my_file2.write('Один\nДва\n')

# Если файла нет, то он создастся
# with open('lesson13/text_file1.txt', 'w', encoding='UTF-8') as my_file2:
#     my_file2.write('Один\nДва\n')

# Для дозаписи откроем с режимом "a" - append, запись без удаления прошлых данных
with open('lesson13/text_file.txt', 'a', encoding='UTF-8') as my_file2:
    my_file2.write('Три\nЧетыре\n')
