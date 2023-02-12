class Fruit:
    """ Базовый класс фрукты"""
    def __init__(self, name: str, fiber: float, calories: int):
        """
        Конструктор
        :param name: str, Название фрукта
        :param fiber: float, Количество клетчатки
        :param calories: int, Количество каллорий
        """

        self.name = name
        self.fiber = fiber
        self.calories = calories

    @property
    def name(self):
        """
        :return: название
        """
        return self.name

    @property
    def fiber(self):
        """
        :return: количество клетчатки
        """
        return self.fiber

    @property
    def calories(self):
        """
        :return: количество клетчатки
        """
        return self.calories

    def __str__(self):
        return f"Фрукт {self.name}. Клетчатка {self.fiber}. Калории {self.calories}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, fiber={self.fiber!r})"

    def Juice(self,i:int):
        """
        Сок из фруктов
        """
        if i is None:
            print('c мякотью')
        else:
            print('без мякоти')



class Apple(Fruit):
    def __init__(self,  fructose: float, name):
        """

        :param fructose: Количество фрутозы
        :param kwargs: Наследуемые аргументы
        """
        if not isinstance(fructose, float):
            raise TypeError("fructose должна быть типа float ")

        super().__init__(name,44.,65.)
        self.fructose = fructose

    def __str__(self):
        return f"Фрукт {self.name}. Клетчатка {self.fiber}. Калории {self.calories}"


class Orange(Fruit):
    def __init__(self,  vitamin: float):
        """

        :param vitamin: Количество vitamin
        :param kwargs: Наследуемые аргументы
        """
        if not isinstance(vitamin, float):
            raise TypeError("vitamin должна быть типа  float")
        self.vitamin = vitamin

    def __str__(self):
        return f"Фрукт {self.name}. Клетчатка {self.fiber}. Калории {self.calories}"

def main():
    a = Apple(10., 'apple')
    a.__str__()
    a.__repr__()

    o = Orange()
    o.__str__()
    o.__repr__()
    o.Juice()
    o.Juice(1)

if __name__ == "__main__":
    main()