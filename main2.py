from abc import ABC, abstractmethod


class ITaxCalculator(ABC):
    @abstractmethod
    def calculate_tax(self):
        ...


class TaxCalculator2023(ITaxCalculator):
    def calculate_tax(self):
        return 0


class TaxCalculator2024(ITaxCalculator):
    def calculate_tax(self):
        return 0



class Main:
    @staticmethod
    def main(calc: ITaxCalculator) -> float:
        calculator = calc
        tax = calculator.calculate_tax()
        return tax

#
# res = Main.main(TaxCalculator2023())
# print(res)

res = Main.main(TaxCalculator2024())
print(res)
