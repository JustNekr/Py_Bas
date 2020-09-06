'''
Очень надеюсь что я правильно понял про аналогию с последним примером.
у меня чуть голова не взорвалась, пока я думал, что в саомй __init__
должна создаваться только одна переменная self.data, а потом уже из нее как-то
метод класса должен извлекать и превращать строки в цифры и куда-то их записывать
и каким вообще боком потом статический метод должен их достать и обработать
'''


class Data:

    def __init__(self, dd, mm, yy):
        self.dd = dd
        self.mm = mm
        self.yy = yy


    def __str__(self):
        return f'{self.dd}.{self.mm}.{self.yy}'


    @classmethod
    def to_int(cls, data):
        try:
            dd, mm, yy = map(int, data.split('-'))
        except Exception:
            print('некорректный ввод')
        else:
            return cls(dd, mm, yy)


    @staticmethod
    def valid(self):
        if self.dd > 31:
            self.dd = 31
        if self.mm > 12:
            self.mm = 12
        return self


m = '35-13-1985'
m1 = Data.to_int('3ваыва4-13-1985')
Data.valid(Data.to_int(m))
print(Data.valid(Data.to_int(m)))
