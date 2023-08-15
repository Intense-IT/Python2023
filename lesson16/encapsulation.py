# Инкапсуляция - принцип ООП, сокрытие данных,
# подразумевающий ограничение прямого доступа к данным.

# Базовые понятия: геттер (getter) и сеттер (setter) -
# позволяют настраивать доступ, считывание и запись, к данным

class Bank_account:
    def __init__(self, name, money):
        self.name = name
        # свойство __money, хранящее количество денег, скрыто
        self.__money = money

    # Создадим общедоступное свойство public_money

    # реализуем геттер к public_money через @property
    @property
    def public_money(self):
        check = input('Введите пароль: ')
        if check == '1234':
            return self.__money
        else:
            return 'У вас нет доступа к данной информации.'

    # реализуем сеттер к public_money через @public_money.setter
    @public_money.setter
    def public_money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('У вас ошибка в данных')


# создаем экземпляр класса Bank_account
me = Bank_account('Саид', 1000)

# print(me.__money)  # выдаст ошибку
print(me.public_money)
me.public_money = 'qwer'
print(me.public_money)
