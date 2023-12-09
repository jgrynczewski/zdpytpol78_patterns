# Paradygmat: proceduralny, funkcyjny, obiektowy
# 1. DRY - Don't Repeate Yourself
# Rule of three ("Three strikes and you refactor")
# Funkcja - nazwany blok kodu
# Klasa - zbiór cech (atrybutów) i umiejętności (metod)

# __new__ - konstruktor klasy (tworzy wydmuszkę)
# __init__ - inicjalizator klasy (inicjalizuje wartości)

class Auto:
    def __init__(self, name, age):
        # obiektowe atrybuty (zbiór atrybutów = stan obiektu)
        self.name = name
        self.age = age
        self.is_empty = True

    # obiektowe metody (modyfikują/odczytują stan obiektu)
    def start(self):
        if self.is_empty:
            print("Sorry, I'm empty")
        else:
            print("Brum brum brum")

    def introduce_yourself(self):
        print(f"Hello, my name is {self.name}")

    def fill(self):
        self.is_empty = False
        print("Oh, thanks!")

    @staticmethod
    def get_circle_area(r):
        return 3.14 * r ** 2


class Service:
    def __init__(self, cars):
        self.cars = cars


class Mechanic:
    def repair(self, car):
        ...


a1 = Auto("ZigZag", 2)
a2 = Auto("Ben", 5)

a1.start()
a1.fill()
a1.start()

res = a2.get_circle_area(1)
print(res)

# Interfejs
# Dziedziczenie (IS-A) - inheritance

# Kompozycja (HAS-A) - composition - (szczególny przypadek - Agregacja, bo wiele cars)
s1 = Service([a1, a2])

# Zależość (USE-A) - dependency
m = Mechanic().repair(a1)


# 2. KISS - Keep It Simple, Stupid
# 3. YAGNI - You ain't gonna need it
# 4. SoC - Separation of Concern

