import os

# Наследование (Inheritance) - принцип, согласно которому новый класс может быть создан на основе существующего класса,
# заимствуя его свойства и методы, чтобы избежать дублирования кода.

# Пример без Наследования


class Cow:
    def __init__(self, name):
        self.__name = name  # инкапсуляция

    def speak(self):
        return "Moo!"


class Dog:
    def __init__(self, name):
        self.__name = name  # инкапсуляция

    def speak(self):
        return "Woof!"


class Cat:
    def __init__(self, name):
        self.__name = name  # инкапсуляция

    def speak(self):
        return "Meow!"


def main():
    cow = Cow("Маруся")
    print(cow.speak())

    dog = Dog("Шарик")
    print(dog.speak())

    cat = Cat("Мурзик")
    print(cat.speak())


if __name__ == '__main__':
    os.system('cls||clear')
    main()
