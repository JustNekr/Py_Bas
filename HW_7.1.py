"""
Ничего понятного про сложение матриц в интернете не нашел
Хотя лет 14 назад даже начанал их проходить в универе
и я так понимаю, что есть какое-то простое решение, даже в случае
если это будут списки со списками списков?
по идее тут рекурсивная функция нужна
но я пока никак не могу описать,
когда именно ей перестать вызывать себя и выдать значение
вот что пока надумал но не работает
    def __add__(self, other):
        if self.matrix and other.matrix is int:
            return self.matrix + other.matrix
        elif len(self.matrix) == len(other.matrix):
            new = []
            for i, j in zip(self.matrix, other.matrix):
                new.append(Matrix(i) + Matrix(j))
            return Matrix(new)

        else:
            return 'неккоректное сложение матриц'
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return ''.join(map(str, [' '.join(map(str, [f'{i:03}' for i in el])) + "\n" for el in self.matrix]))

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            new = []
            for i, j in zip(self.matrix, other.matrix):
                new2 = []
                for a, b in zip(i, j):
                    new2.append(a + b)
                new.append(new2)
            return Matrix(new)
        else:
            return 'неккоректное сложение матриц'


m = Matrix([[1, 2], [3, 4], [5, 6]])
m2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(m)

m3 = m + m2
print(m3)
