class Burger:
    def __init__(self, bun, patty, cheese):
        self.bun = bun
        self.patty = patty
        self.cheese = cheese



class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None

    def set_bun(self, bun_style):
        self.bun = bun_style

    def set_patty(self, patty_style):
        self.patty = patty_style

    def set_cheese(self, cheese_style):
        self.cheese = cheese_style


class BuilderBurger:
    def __init__(self):
        self.burger = Burger()

    def add_bun(self, bun_style):
        self.burger.set_bun(bun_style)
        return self

    def add_patty(self, patty_style):
        self.burger.set_patty(patty_style)
        return self

    def add_cheese(self, cheese_style):
        self.burger.set_cheese(cheese_style)
        return self

    def build(self):
        return self.burger

####################################################
# fluent interface - methods chaining (łańcuchowanie metod)
drwal = BuilderBurger()\
    .add_bun('cheese and bacon bun')\
    .add_patty('beef')\
    .add_cheese('cheese panckage')\
    .build()


print(drwal)
