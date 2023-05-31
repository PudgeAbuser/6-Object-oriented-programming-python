import os

# Абстракция (Abstraction) - Сокрытие деталей реализации и предоставление только необходимых сведений (Simplicity)
# - принцип, согласно которому объекты моделируются только со стороны, которая необходима для решения конкретной задачи,
# а ненужные детали скрываются.

# Пример без Абстракции


class Animal():
    def make_sound(self):  # нет необходимости переопределять
        print('Foo')


class Dog(Animal):
    def move(self):
        print('Move dog')


def main():
    anim = Animal()  # ошибки нет
    anim.make_sound()

    dog = Dog()
    dog.make_sound()
    dog.move()


if __name__ == '__main__':
    os.system('cls||clear')
    main()
