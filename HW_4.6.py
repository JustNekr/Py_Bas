from sys import argv
from itertools import cycle, count, repeat

my_list = []
c = 0
for el in count(int(argv[1])):  # генерирует с помощью итератора список в пределах заданных в параметрах
    if el > int(argv[2]):
        break
    else:
        my_list.append(el)
print(my_list)
for el in cycle(my_list):  # повторяет элементы ранее заданного списка, заданное в параметре количество раз
    if c > int(argv[2]):
        break
    else:
        print(el)
        c += 1

itr = iter(range(int(argv[1]), int(argv[2]) + 1))  # если я вас верно понял это то как сделать без брэйка
print(itr)
for i in itr:
    print(i)


