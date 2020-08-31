class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self, kg, sm):
        print(f'На строительство такой дороги уйдет {self._length * self._width * kg * sm / 1000} тонн асфальта')


a = Road(5000, 20)
a.mass(25, 5)
b = Road(2000, 20)
b.mass(13, 4)
