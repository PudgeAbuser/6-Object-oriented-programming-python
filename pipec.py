class Human:
    def __init__(self,name,age,gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def infoHuman(self):
        return f"{self.__name} {self.__age} {self.__gender}"
    
    @infoHuman.setter
    def infoHuman(self, value):
        if 1 <= value <= 17:
            self.__age = value
        else:
            print("Ничего не работает")


    @property
    def gender(self):
        return self.__age
    
    @gender.setter
    def gender(self, value):
        if value == "м" or value == "ж":
            self.__gender = value
        else:
            raise ValueError("Не сработало")
    


def main():
    name1 = Human("Давид", 17, "man")
    name1.infoHuman = int(input("Введите возраст: "))
    print(name1.gender)
    gender = input("Введите ваш пол: ")
    name1.gender = gender
    print(name1.gender)
    print(name1.infoHuman)
   
    


if __name__ == '__main__':
    main()