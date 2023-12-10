class Burger:
    def __init__(self, ingredients: list[str]):
        self.ingredients = ingredients


b1 = Burger(['wheat ban', 'beef', 'pickle'])


class BurgerFactory:
    """Inicjalizuje burgera i zwraca go nam"""
    def create_hamburger(self) -> Burger:
        ingredients = ['wheat bun', 'beef', 'pickle']
        return Burger(ingredients)

    def create_mcrolay(self) -> Burger:
        ingredients = ['wheat bun', 'beef', 'pickle', 'cheddar cheese']
        return Burger(ingredients)

    def create_drwal(self) -> Burger:
        ingredients = ['cheese and bacon bun', 'beef', 'pickle', 'cheese pancake']
        return Burger(ingredients)

######################################################################

b2 = BurgerFactory().create_hamburger()
b3 = BurgerFactory().create_mcrolay()


print(b2)
