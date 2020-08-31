class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')

    def get_total_income(self):
        print(f'Полный доход составит: {sum(self._income.values())} у.е.')


a = Position('павел', 'майор', 'оператор', 25.05, 36.05)
a.get_full_name()
a.get_total_income()
"""Почему при таких значениях вместо 61.1 он выдает такой странный результат 
Полный доход составит: 61.099999999999994 у.е.???"""
