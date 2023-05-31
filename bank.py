class Cart:
    def __init__(self, mark, kuzov, vipusk):
        self.__mark = mark
        self.__kuzov = kuzov
        self.__vipusk = vipusk

    @property
    def infocar(self):
        return f"{self.__mark} {self.__kuzov} {self.__vipusk}"
    
    @infocar.setter
    def infocar(self,marka):
        marka = "BMW"
        if marka == "BMW":
            self.__mark = marka
        else:
            raise ValueError("Не та марка!")

def main():
    god1 = Cart("bmw","M5 F90","cs2020")
    god1.infocar = input('ВВедите лучшую марку авто: ')
    print(god1.infocar)

if __name__ == "__main__":
    main()