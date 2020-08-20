def devision(a, b):
    """делит а на b"""
    if b == 0:
        b = float(input('на 0 делить невозможно, введите другое число'))
        devision(a, b)
    else:
        # c = a / b JS из основ программировния вечно сбивает
        print(f'{a}/{b}={(a / b):.3f}')


devision(float(input('введите делимое')), float(input('введите делитель')))


####################################Version_2#########################################

def devision(a, b):
    """делит а на b"""
    try:
        print(f'{a}/{b}={(a / b):.3f}')
    except ZeroDivisionError:
        b = float(input('на 0 делить невозможно, введите другое число'))
        devision(a, b)


devision(float(input('введите делимое')), float(input('введите делитель')))
