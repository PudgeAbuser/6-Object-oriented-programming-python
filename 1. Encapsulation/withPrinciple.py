import os

# Инкапсуляция (Encapsulation) - принцип, согласно которому данные (переменные) и методы (функции)
# для работы с ними объединяются в единый объект (класс) и скрыты от прямого доступа извне,
# чтобы избежать изменений внутренней реализации класса.

# В ООП инкапсуляция означает, что данные и методы, которые работают с этими данными,
# должны быть скрыты от внешнего мира и доступны только внутри класса.
# То есть, данные должны быть защищены от прямого доступа извне,
# а операции над ними должны выполняться через методы класса.

# Пример с инкапсуляцией


class Player:
    def __init__(self, name, lvl):
        self.__name = name  # защищенная переменная класса (инкапсуляция)
        self.__lvl = lvl

    # первый вариант записи, но препятствуют принципу ООП - инкапсуляции
    def getLvl(self):
        return self.__lvl

    def setLvl(self, lvl):
        self.__lvl = lvl

    # второй вариант более правильнее, т.к является более новым и удобным для поддержки
    @property
    def lvl(self):
        return self.__lvl

    @lvl.setter
    def lvl(self, value):
        if 1 <= value <= 100:
            self.__lvl = value
        else:
            raise ValueError("Уровень должен быть между 1 и 100")


def main():
    player = Player("Игрок1", 50)
    print(player.getLvl())
    print(player.lvl)  # 50

    player.lvl = 80
    player.setLvl(100)
    print(player.lvl)  # 80

    # player.lvl = 120  # ValueError: Уровень должен быть между 1 и 100


if __name__ == '__main__':
    os.system('cls||clear')
    main()
