class Soda:
    """Класс газировки для определения ее типа"""

    def __init__(self, additive=None):
        self.additive = additive

    def show_my_drink(self):
        if self.additive:
            return "Газировка и " + self.additive
        return 'Обычная газировка'


gaz = Soda()
print(gaz.show_my_drink())
