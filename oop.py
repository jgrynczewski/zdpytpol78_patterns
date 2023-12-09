# Polimorfizm - wielopostaciowość

# type hints (type annotation)
x: int = 4


class Dog:
    def speak(self):
        print("Hau hau")


class Cat:
    def speak(self):
        print("Miau miau")


class Horse:
    def speak(self):
        print("Ihaaaaa")


def give_voice(x):
    x.speak()


zoo = [Dog(), Cat(), Horse()]
for animal in zoo:
    give_voice(animal)


# walidacja typu (to może być antywzorzec)
# x = 4
# if type(x) != int:
#     raise Exception
# if isinstance(x, int):
#     raise Exception
