from sys import argv
"""я вообще не понял что надо сделать в этом задании
но как резултат создается генератор из него извлекаются и выводятся все значани 
и перемножаются друг на друг на друга, и как результат:
факториал заданного в параметрах числа
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)"""
def fact(n):
    for el in range(1, n + 1):
        yield el
global c
c = 1
for el in fact(int(argv[1])):
    print(el)
    c = c * el
print(c)
