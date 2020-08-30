"""Очень понравилась идея уместить все решение в одну строку
не списывал с того что в видео есть, просто дописал в уже начатое решение"""
with open('text_6.txt', 'r', encoding='utf-8') as file:
    x = file.readlines()
    print(x)
    my_dict = {
        i[0: i.find(':')]: sum(map(int, ''.join([el if '0' <= el <= '9' else ' ' for el in i[i.find(':'):]]).split()))
        for i in x}
print(my_dict)
