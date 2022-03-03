from contracts import contract

class Soda:
    def __init__(self, drink):
        self.drink = drink
    #@contract(a = 'int,>=0')
    def show_my_drink(self, a:int):
        if a <= 0 or not isinstance(a, int):
            raise ValueError(f'expecting positive integer in parameter[a], got: {a}')

Soda('Kola').show_my_drink(-1)
