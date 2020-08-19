my_list = [7, 5, 3, 3, 2, 1]
while True:
    number = int(input('введите число от 0 до 9'))
    for ind, el in enumerate(my_list):
        if number > el:
            my_list.insert(ind, number)
            break
    else:
        my_list.append(number)
    print(my_list)


