from abc import ABC, abstractmethod
"""
Не стал в итоге реализовывать абстрактный метод
иначе для общего подсчета не видел другого варината как создавать список либо так же словарь
вне родительского класса и при создании добавлять туда результаты работы how_much
а так я через один контейнер все и создаю и добавляю и вывожу.
При работе же с абстракцией контейнер не получился бы, 
ибо как я понял абстрактный класс инициализировать нельзя.
И еще, с формулами подсчета у меня не сложилось, я не понимаю какие должны быть
критерии к вводимым значениям, ну и как понял так и ограничил
15 < размер < 66
150 < рост <220
Хотя результат вообще неадекватный получается
"""

class Clothes(ABC):

    def __init__(self, name='Одежда'):
        self.name = name
        self.vsego = {'Пальто': [], 'Костюмы': []}

    @property
    def how_much(self):

        print(f'Ткани для пальто потребуется: {round(sum(self.vsego["Пальто"]))} \n Для костюмов: {round(sum(self.vsego["Костюмы"]))} ')

    @property
    def add(self):
        kind = input('what kind of clothes U wanna add? \n P for Palto / K for Kostum')
        if kind.lower() == 'p':
            self.vsego['Пальто'].append(Palto(int(input('введите размер пальто: '))).how_much)

        elif kind.lower() == 'k':
            self.vsego['Костюмы'].append(Kostum(int(input('введите рост костюма: '))).how_much)



class Palto(Clothes):
    def __init__(self, V, name="Пальто"):
        self.name = name
        self.V = V

    @property
    def how_much(self):
        return self.V / 6.5 + 0.5

    @property
    def V(self):
        return self.__V

    @V.setter
    def V(self, V):
        if V < 15:
            self.__V = 15
        elif V > 66:
            self.__V = 66
        else:
            self.__V = V


class Kostum(Clothes):
    def __init__(self, H, name="Костюм"):
        self.name = name
        self.H = H

    @property
    def how_much(self):
        return 2 * self.H + 0.3

    @property
    def H(self):
        return self.__H

    @H.setter
    def H(self, H):
        if H < 150:
            self.__H = 150
        elif H > 220:
            self.__H = 220
        else:
            self.__H = H


c = Clothes()
c.add
c.add
c.add
c.add
c.add
c.add


c.how_much
