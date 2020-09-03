class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell < other.cell:
            print('WARNING!!! its imposible')
        else:
            return Cell(self.cell - other.cell)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(round(self.cell / other.cell))

    def make_order(self, rows):
        if self.cell % rows == 0:
            for i in range(self.cell // rows):
                print(f'{"*" * rows}')
        else:
            for i in range(self.cell // rows):
                print(f'{"*" * rows}')
            print(f'{"*" * (self.cell % rows)}')


a = Cell(6)
b = Cell(35)
c = Cell(25)
d = a + b
d.make_order(5)