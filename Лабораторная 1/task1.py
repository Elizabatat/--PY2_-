import doctest

class Monkey_fight:

    def __init__(self, m1, m2):
        """  Создание и подготовка к работе объекта "Обезьяний бой"

        :param m1: Масса первой обезьянки
        :param m2: Масса второй обезьянки
        """
        if not isinstance(m1, (int, float), m2, (int, float)):
            raise TypeError("Масса должна быть типа int или float")
        self.baby_monkey1 = m1
        self.baby_monkey2 = m2

    def fight(self, p=50):
        """ Функция проверяет какая из обезьянок с заданной массой проиграет в битве
         :param p: int, вероятность ничьей
         :return: int или float, масса проигравшей обезьянки
          """
        pass

    def feed(self, food):
        """ Функция увеличения массы проигравшей обезьянки
            :return: int или float, новая масса обезьянки
            """
        m = self.fight()
        if self.m1 == m:
            self.m1 = m + food
        else:
            self.m2 = m + food
        pass

class Horse_jumping_competition:

    def __init__(self, v, h):
        """ Создание и подготовка к работе объекта "Лошадный конкур"

           :param m1: Скорость
           :param m2: Высота прыжка"""
        self.velocity = v
        self.high = h

    def gallop(self, track):
        """ Функция проверяет за какое время лошадь достигнет финиша
                 :param trck: дистанция
                 :return: int или float, время
                  """
        pass

    def jump(self, track):
        """ Функция проверяет максимальную высоту прыжка

                 :return: int или float, высота
                  """
        pass


class Bat:

    def __init__(self, t, e):
        """  Создание и подготовка к работе объекта "Летучая мышь"

           :param m1: время сна
           :param m2: голод
           """

        self.sleep = t
        self.hunger = e

    def wake_up(self):
        """ Функция проверяет максимальную голод летучей мыши и,
        если он достигает максимального значения, мышь просыпается
         :return: True - мышь спит, False - мышь проснулась
                         """
        pass



if __name__ == "__main__":
    doctest.testmod()
