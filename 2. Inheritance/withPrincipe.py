import os

# Наследование (Inheritance) - принцип, согласно которому новый класс может быть создан на основе существующего класса,
# заимствуя его свойства и методы, чтобы избежать дублирования кода.

# Пример c Наследованием


class Animal:
    def __init__(self, name):
        self.__name = name  # инкапсуляция

    @property
    def name(self):
        return self.__name

    def speak(self):
        return "Rrr"


class Cow(Animal):
    def eat(self):
        return f"{self.name}: cow eat";

    def speak(self):
        return "Moo!"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def main():
    cow = Cow("Маруся")
    print(cow.speak())
    print(cow.eat())

    dog = Dog("Шарик")
    print(dog.speak())

    cat = Cat("Мурзик")
    print(cat.speak())
    print(cat.speak2())


if __name__ == '__main__':
    os.system('cls||clear')
    main()
