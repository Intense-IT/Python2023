# Проверка на палиндром

def palindrome(text=''):  # параметру задано значение по умолчанию
    return text == text[::-1]


print(palindrome('шалаш'))
print(palindrome('текст'))
print(palindrome())
