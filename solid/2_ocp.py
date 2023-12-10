# Open Close Principle
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p


############################################################

apple = Product("Apple", Color.GREEN, Size.SMALL)
tree = Product("Tree", Color.GREEN, Size.LARGE)
house = Product("House", Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
for p in pf.filter_by_color(products, Color.GREEN):
    print(f"- {p.name} is green")

for p in pf.filter_by_size(products, Size.LARGE):
    print(f"- {p.name} is large")

for p in pf.filter_by_size_and_color(products, Size.LARGE, Color.BLUE):
    print(f"- {p.name} is large and blue")


# Wzorzec specyfikac
from abc import ABC, abstractmethod


class ISpecification(ABC):
    @abstractmethod
    def is_satisfy(self, product):
        ...


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfy(self, product):
        return product.color == self.color


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfy(self, product):
        return product.size == self.size


class NewFilter:
    def filter(self, products, specification: ISpecification):
        for p in products:
            if specification.is_satisfy(p):
                yield p


#####################################################################

nf = NewFilter()
for p in nf.filter(products, ColorSpecification(Color.GREEN)) :
    print(f"- {p.name} is green")

for p in nf.filter(products, SizeSpecification(Size.LARGE)) :
    print(f"- {p.name} is large")
