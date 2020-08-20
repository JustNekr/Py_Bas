def my_funct(*args):
    sum = args[1]
    args = args[0].split()
    for el in args:
        if el != "q":
            sum += float(el)
        else:
            return print(sum)
    print(sum)
    my_funct(input('Введите числа разделенные пробелами, для завершения введите "Q": '), sum)


my_funct(input('Введите числа разделенные пробелами, для завершения введите "Q": '), 0)

# Как же долго я понимал что вводимая инпутом при первом вызове функции строка становится лишь первым элементом кортежа arags
