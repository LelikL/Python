from abc import ABC, abstractmethod


class Clothes(ABC):
    # attribute
    def __init__(self, param):
        self.param = param

    calc = 0

    # method
    @property
    @abstractmethod
    def calculation(self):
        pass

    def __str__(self):
        res = Clothes.calc
        Clothes.calc = 0
        return f"{res}"

    def __add__(self, other):
        Clothes.calc += self.calculation + other.calculation
        return Costume(0)


class Coat(Clothes):
    # method
    @property
    def calculation(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    # method
    @property
    def calculation(self):
        return round((self.param / 100) * 2 + 0.3)


coat = Coat(40)
costume = Costume(240)
print(f'Общий расход ткани составит: {coat + costume}')

