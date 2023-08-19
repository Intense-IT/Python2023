# Наследование - принцип ООП

# Класс Animal
class Animal:
    def __init__(self, nickname):
        self.nickname = nickname
        self.paws = 4

    def run(self):
        print('Побежала!')

    def sound(self):
        print('Визг!')


# Класс Cat, дочерний классу Animal
class Cat(Animal):
    def sound(self):  # перезапись метода sound()
        print('Мяу')


# Класс Dog, дочерний классу Animal
class Dog(Animal):
    def sound(self):
        print('Гав-гав!')

    # новый метод
    def bite(self):
        print('УКУСИЛА!')


# Класс Shepherd, дочерний классу Dog
class Shepherd(Dog):
    # Метод __init__() перезаписывается
    def __init__(self, nickname, ancestry):
        # super() говорит, что брать метод (__init__) надо у родителя
        super().__init__(nickname)
        # строчка выше заменяет задание self.nickname и self.paws
        self.ancestry = ancestry

    def sound(self):
        print('Ррррав!')

    def bite(self):
        super().bite()  # вызывается метод bite родительского класса
        print('Гонит овец к стаду.')  # доп. действия


# Создаем экземпляр класса Cat
cat = Cat('Пушок')
cat.run()  # метод run достался от Animal без изменений
cat.sound()  # метод sound у объекта от класса Cat

# Создаем экземпляр класса Dog
dog = Dog('Барбос')
dog.run()  # метод run достался от Animal без изменений
dog.sound()  # метод sound у объекта от класса Dog
dog.bite()  # метод bite у объекта от класса Dog

# Создаем экземпляр класса Shepherd
shepherd_dog = Shepherd('Тузик', 'чистокровный')
shepherd_dog.run()  # метод run достался от Animal без изменений
shepherd_dog.sound()  # метод sound у объекта от класса Shepherd
shepherd_dog.bite()  # метод bite у объекта от класса Shepherd
