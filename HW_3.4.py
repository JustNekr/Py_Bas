def my_func(x, y):
    if y > 0:
        y = int(input('по заданию "Y" должен быть отрицательным, введи снова Y: '))
        return my_func(x, y)
    elif x < 0:
        x = int(input('по заданию "X" должен быть положительным, введи снова  X: '))
        return my_func(x, y)
    else:
        i = 0
        c = 1
        while i < abs(y):
            i += 1
            c = c * x
        return 1 / c


print(my_func(-2, 3))
