from abc import ABC, abstractmethod


class Stock:
    def __init__(self):
        self.stock = {'Принтер': [Printer(), Printer(), Printer()], 'Сканер': [Scanner(), Scanner(), Scanner()],
                      'Ксерокс': [Xerox(), Xerox(), Xerox()]}
        self.company = {'Магазин': [Printer(), Printer(), Scanner(), Xerox(), Xerox(), Xerox()], 'Офис': []}

    @property
    def add_to_stock(self):
        while True:
            what = input(
                'Что хотите добавить на склад? \nВведите "P" для принтера "S" для сканера "X" для ксерокса.\nдля '
                'остановки перемещения введите "q": ')
            try:
                if what.lower() == 'p':
                    for i in range(int(input('В каком количестве поступили принтеры'))):
                        self.stock['Принтер'].append(Printer())
                elif what.lower() == 's':
                    for i in range(int(input('В каком количестве поступили сканеры'))):
                        self.stock['Сканер'].append(Scanner())
                elif what.lower() == 'x':
                    for i in range(int(input('В каком количестве поступили ксероксы'))):
                        self.stock['Ксерокс'].append(Xerox())
                elif what.lower() == 'q':
                    break
                else:
                    print('неккоректный ввод названия техники')
            except ValueError:
                print('Количество введено не верно, ТОЛЬКО ЦЕЛЫЕ ЧИСЛА')

    @property
    def send_from_stock(self):
        while True:
            what = input(
                'Что хотите переместить со склада? \nВведите "P" для принтера "S" для сканера "X" для ксерокса.\nдля '
                'остановки перемещения введите "q": ')

            try:
                if what.lower() == 'p':
                    where = input('Куда перемещаем принетры?\nВведите "M" для магазина "O" для офиса: ')
                    if where.lower() == 'm':
                        for i in range(int(input('В каком количестве перемещаем принтеры'))):
                            self.company['Магазин'].append(self.stock['Принтер'].pop(0))
                    elif where.lower() == 'o':
                        for i in range(int(input('В каком количестве перемещаем принтеры'))):
                            self.company['Офис'].append(self.stock['Принтер'].pop(0))
                    else:
                        print('Некорректный ввод подразделения')
                elif what.lower() == 's':
                    where = input('Куда перемещаем сканеры?\nВведите "M" для магазина "O" для офиса: ')
                    if where.lower() == 'm':
                        for i in range(int(input('В каком количестве перемещаем сканеры'))):
                            self.company['Магазин'].append(self.stock['Сканер'].pop(0))
                    elif where.lower() == 'o':
                        for i in range(int(input('В каком количестве перемещаем принтеры'))):
                            self.company['Офис'].append(self.stock['Сканер'].pop(0))
                    else:
                        print('Некорректный ввод подразделения')
                elif what.lower() == 'x':
                    where = input('Куда перемещаем ксероксы?\nВведите "M" для магазина "O" для офиса: ')
                    if where.lower() == 'm':
                        for i in range(int(input('В каком количестве перемещаем сканеры'))):
                            self.company['Магазин'].append(self.stock['Ксерокс'].pop(0))
                    elif where.lower() == 'o':
                        for i in range(int(input('В каком количестве перемещаем принтеры'))):
                            self.company['Офис'].append(self.stock['Ксерокс'].pop(0))
                    else:
                        print('Некорректный ввод подразделения')
                elif what.lower() == 'q':
                    break
                else:
                    print('неккоректный ввод')
            except ValueError:
                print('Количество введено не верно, ТОЛЬКО ЦЕЛЫЕ ЧИСЛА')
            except IndexError:
                print('Недостаточное количество на складе')

    @property
    def stock_balance(self):
        return f'На складе: {len(self.stock["Принтер"])} шт. принтеров, {len(self.stock["Сканер"])} шт. сканеров,' \
               f' {len(self.stock["Ксерокс"])} шт. ксероксов '

    @property
    def company_balance(self):
        mag = [el.self_name for el in self.company['Магазин']]
        off = [el.self_name for el in self.company['Офис']]
        return f'В магазине: {mag.count("Принтер")} шт. принтеров, {mag.count("Сканер")} шт. сканеров,' \
               f' {mag.count("Ксерокс")} шт. ксероксов.\nВ офисе: {off.count("Принтер")} шт. принтеров,' \
               f' {off.count("Сканер")} шт. сканеров, {off.count("Ксерокс")} шт. ксероксов'


class Office_equipment(ABC):
    def __init__(self, type_name='Оргтехника'):
        self.type_name = type_name

    @abstractmethod
    def what_is_this(self):
        return f'{self.type_name}'


class Printer(Office_equipment):
    def __init__(self, type_name='Оргтехника', self_name='Принтер'):
        super().__init__(type_name)
        self.self_name = self_name

    def what_is_this(self):
        return f'{self.type_name}: {self.self_name}'


class Scanner(Office_equipment):
    def __init__(self, type_name='Оргтехника', self_name='Сканер'):
        super().__init__(type_name)
        self.self_name = self_name

    def what_is_this(self):
        return f'{self.type_name}: {self.self_name}'


class Xerox(Office_equipment):
    def __init__(self, type_name='Оргтехника', self_name='Ксерокс'):
        super().__init__(type_name)
        self.self_name = self_name

    def what_is_this(self):
        return f'{self.type_name}: {self.self_name}'


s = Stock()
print(s.stock_balance)
print(s.company_balance)
s.add_to_stock
s.send_from_stock
print(s.stock_balance)
print(s.company_balance)
