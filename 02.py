from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_consuption(self):
        pass

    @staticmethod
    def get_total_consumption(*clothes):
        """Подсчет суммарного расхода ткани для переданных предметов одежды"""
        for obj in clothes:
            if not isinstance(obj, Clothes):
                raise TypeError(f'Объект {obj} не является одеждой')
        return sum([obj.get_consuption for obj in clothes])


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def get_consuption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def get_consuption(self):
        return self.height * 2 + 0.3


suit = Suit('suit', 10)
print('Расход ткани на костюм:', suit.get_consuption)

coat = Coat('coat', 7.5)
print('Расход ткани на пальто:', round(coat.get_consuption, 2))

print('Общий расход ткани:', round(Clothes.get_total_consumption(suit, coat), 2))
