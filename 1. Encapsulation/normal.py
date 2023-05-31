import os

# Инкапсуляция (Encapsulation) - принцип, согласно которому данные (переменные) и методы (функции)
# для работы с ними объединяются в единый объект (класс) и скрыты от прямого доступа извне,
# чтобы избежать изменений внутренней реализации класса.

# Пример без инкапсуляции

class Player:
    def __init__(self, name, lvl):
        self.name = name
        self.lvl = lvl


def main():
    player = Player("Игрок1", 50)
    player.name = "Игрок Эльдар"
    print(player.name)  # Игрок Эльдар

    player.lvl = 80
    print(player.lvl)  # 80


if __name__ == '__main__':
    os.system('cls||clear')
    main()
