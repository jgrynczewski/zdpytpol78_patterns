from abc import ABC, abstractmethod


class IAnimal(ABC):
    @abstractmethod
    def speak(self):
        ...


class Cow(IAnimal):
    def speak(self):
        print("Muuuuuu")


class Horse(IAnimal):
    def speak(self):
        print("Ihaaa")


class Pig(IAnimal):
    def speak(self):
        ...


############################################################

Cow()
Horse()
Pig()
