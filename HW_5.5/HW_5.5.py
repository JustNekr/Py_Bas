import random
from sys import argv
with open('new_file.txt', 'w', encoding='utf-8') as file:
    my_list = []
    for i in range(0, int(argv[1])):
        my_list.append(str(random.randint(0, int(argv[2]))))
    my_list = (' '.join(my_list))
    print(my_list, file=file)

with open('new_file.txt', 'r', encoding='utf=8') as file:
    c = file.read().split()
    new_list = [int(el) for el in c]
    # print(new_list)
    # print(type(new_list))
    print(sum(new_list))