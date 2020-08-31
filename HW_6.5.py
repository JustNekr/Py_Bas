class Stationery:
    def __init__(self, title='название'):
        self.title = title

    def draw(self):
        print('запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title='ручкой'):
        self.title = title
    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Pencil(Stationery):
    def __init__(self, title='карандашом'):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки {self.title}')


class Handle(Stationery):
    def __init__(self, title='маркером'):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки {self.title}')

p = Pen()
pl = Pencil()
h = Handle()
p.draw()
pl.draw()
h.draw()