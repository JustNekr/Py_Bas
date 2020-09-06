'''
почему, если при создании своего исключения,
еслия сразу присвою значение переменной self.txt='на ноль делить нельзя'
либо в скобках txt='на ноль делить нельзя'
а при rise MyError() оставлю скобки пустыми,
то он не выводит никакого сообщения?
я вообще правильно понимаю, что райз как бы создает объект класса MyError
или это не верно?
'''


class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    a = input('введите  делимое')
    b = input('введите  делитель')
    try:
        a, b = map(int, (a, b))
        if b == 0:
            raise MyError('на ноль делить нельзя')
    except ValueError:
        print('введите число')
    except MyError as err:
        print(err)
    else:
        print(f'результат: {a / b}')
