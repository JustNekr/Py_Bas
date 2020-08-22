from functools import reduce
def func(el1, el2):
    return el1 * el2
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(func, my_list))