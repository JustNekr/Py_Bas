def int_func(slovo):
    if slovo.islower():
        slovo = slovo.title()
        return slovo
    else:
        slovo = input(f"в слове {slovo} все буквы должны быть строчными введите его заново: ")
        return int_func(slovo)


def big_int_func(slova):
    slova = slova.split()
    result = []
    for i in slova:
        i = int_func(i)
        result.append(i)
    return (' '.join(result))


c = input("ведите слово")
print(int_func(c))
print(big_int_func(input("введите несколько слов слов")))

# надеюсь не страшно что тут все на встроеных функциях, а не через юникод
# начал через него делать даже нашел что чтобы поставить букву в ерхний регистр нужно из кода 32 вычесть
# но по времени уже припозднился со сдачей
