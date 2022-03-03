class Tomato:
    states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']

    def __init__(self, index=0):
        self._index = index
        self._state = self.states[index]

    def grow(self):
        i = self._index
        self._state = self.states[i]
        self._index += 1

    def is_ripe(self):
        if self._state == 'Красный':
            print('Томат созрел')
        else:
            print('Томат еще не созрел')


class TomatoBush(Tomato):
    def __init__(self, quantity):
        self.quantity = quantity
        self.tomatoes = []

        for i in range(quantity):
            self.tomatoes.append(Tomato())

    def grow_all(self):
        for i in self.tomatoes:
            i._index += 1

    def all_are_ripe(self) -> bool:
        count = 0
        for i in self.tomatoes:
            if i._state == 'Красный':
                count += 1

        if count-1 == len(self.tomatoes):
            return True
        else:
            return False

    def give_away_all(self):
        if self.all_are_ripe():
            self.tomatoes.clear()


class Gardener:
    """Садовник"""
    def __init__(self, name, Tomato: Tomato):
        self.name = name
        self._plant = Tomato

    def work(self):
        i = self._index
        self._state = self.states[i]
        self._index += 1






