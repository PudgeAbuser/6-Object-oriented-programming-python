import os
from abc import ABC, abstractmethod

# Абстракция (Abstraction) - Сокрытие деталей реализации и предоставление только необходимых сведений (Simplicity)
# - принцип, согласно которому объекты моделируются только со стороны, которая необходима для решения конкретной задачи,
# а ненужные детали скрываются.

# Пример c Абстракцией

# необходимо указывать класс ABC для строгой абстракции


class Animal(ABC):
    __LVL, __HEALTH = 1, 100

    # необходимо реализовать в классе наследнике
    @abstractmethod
    def make_sound(self):
        print('Foo')

    # свойство get
    @property
    def getCharacteristics(self):
        return self.__LVL, self.__HEALTH

    # Метод класса является методом,
    # который вызывается не на экземпляре класса,
    # а на самом классе.
    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = lvl
        cls.__HEALTH = health


class Dog(Animal):
    def make_sound(self):
        print('Woof!')

    def move(self):
        print('Move dog')

    def showCharacteristics(self):
        lvl = super().getCharacteristics[0]
        health = super().getCharacteristics[1]
        print(f"Health = {lvl}, LVL = {health}")


class Cat(Dog):
    def make_sound(self):
        print('Meow!')

    def move(self):
        print('Move cat')


def main():
    # ошибка есть поскольку абстрактный класс не может быть создан как объект:
    # anim = Animal()
    # anim.make_sound()

    Animal.set_cls_field(5, 100)  # первый вариант записи (глобальный)
    dog = Dog()
    dog.make_sound()  # Woof!
    dog.move()  # Move dog
    dog.showCharacteristics()  # Health = 5, LVL = 100

    print('\n')

    Animal.set_cls_field(5, 80)  # первый вариант записи
    cat = Cat()
    # cat.set_cls_field(5, 100) # второй вариант записи (локальный)
    cat.make_sound()  # Meow!
    cat.move()  # Move cat
    cat.showCharacteristics()  # Health = 5, LVL = 80


if __name__ == '__main__':
    os.system('cls||clear')
    main()
