# lsp - Liscov Substitiution Principle
from abc import ABC, abstractmethod


class IAnimal(ABC):
    @property
    @abstractmethod
    def num_legs(self):
        pass


class Lion(IAnimal):
    def __init__(self):
        self.__num_legs = 4

    def num_legs(self):
        return self.__num_legs


class Penquin(IAnimal):
    def __init__(self):
        self.__num_legs = 2

    def num_legs(self):
        return self.__num_legs


class Snake(IAnimal):
    def __init__(self):
        self.__num_legs = 0

    def num_legs(self):
        return self.__num_legs


class Herd:
    def __init__(self, animal: IAnimal, num_legs):
        self.animal = animal
        self.num_legs = num_legs

    def count_members(self):
        return int(self.num_legs / self.animal.num_legs())


############################################

herds = [
    Herd(Lion(), 32),
    Herd(Penquin(), 14),
    Herd(Snake(), 8),
]

for h in herds:
    print(f"W stadzie jest {h.count_members()} członków.")
