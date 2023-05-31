import os

# Полиморфизм (Polymorphism) - принцип, согласно которому объекты могут иметь различные формы и поведение,
# даже если они принадлежат к одному и тому же классу.

# Пример без Полиморфизма


class Rectangle:  # Прямоугольник
    def __init__(self, length, width):
        self.__length = length  # инкапсуляция
        self.__width = width  # инкапсуляция

    def area(self):  # считает площадь
        return self.__length * self.__width


class Circle:  # Круг
    def __init__(self, radius):
        self.__radius = radius  # инкапсуляция

    def area(self):  # считает площадь
        return 3.14 * self.__radius ** 2


def main():
    rect = Rectangle(5, 4)
    print(rect.area())

    cir = Circle(5)
    print(cir.area())


if __name__ == '__main__':
    os.system('cls||clear')
    main()
