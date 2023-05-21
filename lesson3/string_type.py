# работа со строками
title = "Фильм \"Мстители\"" # Фильм "Мстители"
print(title)
print(title[0])
# title[0] = "ф" # даст ошибку
print(title[0:5])
print(title[6:16])
print(title[:5]) # аналогичен 5 строке
print(title[6:]) # аналогичен 6 строке
print(title[-2])
print(title[-9:-1])
print(title[:1000])
# print(title[1000]) # даст ошибку
print(title[:])
print(title[6:16:2])
print(title[::-1])

print(len(title)) # команда len возвращает длину строки

many_strings = """Лба твоего просторная поляна,
А чуть пониже, около нее,—
Два озера, как будто два Севана.
Два озера — томление мое."""

print(many_strings)