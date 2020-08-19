words = input('введите слова через пробел: ')
words_list = words.split(' ')
print(words_list)
for ind, el in enumerate(words_list):
    if len(el) > 10:
        print(ind + 1, el[0:10])
    else:
        print(ind + 1, el)
        print(type(ind))
        print(type(el))