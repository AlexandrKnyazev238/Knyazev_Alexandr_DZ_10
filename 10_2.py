# Task_2

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        return self.calculation + other.calculation


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('На детей не шьем. Начинаем от сорокового.')
            self.__size = 40
        elif size > 58:
            print('58 - максимальный размер.')
            self.__size = 58
        else:
            self.__size = size

    @property
    def calculation(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('На детей не шьем.')
            self.__height = 150
        elif height > 240:
            print('240 - максимальный размер.')
            self.__height = 240
        else:
            self.__height = height

    @property
    def calculation(self):
        return 2 * (self.__height / 100) + 0.3


coat_1 = Coat(int(input('Введите размер пальто для рассчета: ')))
print(f'Вам потребуется {coat_1.calculation:.2f} метров ткани на пальто {coat_1.size} размера ')
costume_1 = Costume(int(input('Введите ваш рост для рассчета костюма (в сантиметрах): ')))
print(f'Вам потребуется {costume_1.calculation:.2f} метров ткани на костюм {costume_1.height} роста ')
print(f'Всего вам понадобится {coat_1 + costume_1:.2f} метров ткани.')
