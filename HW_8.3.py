class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False

c = []

while True:
    a = input('введите  число')
    try:
        if a == 'stop':
            print(c)
            break
        elif is_digit(a) == False:
            raise MyError('не текст а число')
        else:
            c.append(float(a))
    except MyError as err:
        print(err)
