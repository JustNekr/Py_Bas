class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}i'

    def __add__(self, other):
        return Complex((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return Complex((self.a * other.a - self.b * other.b), (self.b * other.a + self.a * other.b))

a = Complex(3, 4)
b = Complex(5, 6)
print(a)
print(b)
print(a + b)
print(a * b)
