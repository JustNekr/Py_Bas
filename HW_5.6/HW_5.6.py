"""Только сегодня утром смог приступить к выполнению ДЗ,
и на данный момент остался один час до следющего занятия.
уже понял что дальше в этом задании делать, но написать уже точно не успею.
там надо пробежаться по строке из значения словаря, проверить каждый символ на isNuN
и как-то создать списки из них.
В общем, завтра уже доделаю. Толкьо как их вам потом докинуть?"""

#s = "text text: one two three"
# с = (s.find(":"))
# print(c)
print(s[0 : s.find(":")])
print(type(s[0 : s.find(":")]))

with open('text_6.txt', 'r', encoding='utf-8') as file:
    x = file.readlines()
    print(x)
    for
    my_dict = {i[0 : i.find(':')]: i[i.find(':') : ] for i in x}
    print(my_dict)
    # for i in x:
    #     c = i[0 : i.find(':')]
    #     print(c)
    #     print(i[0 : i.find(':')])
    #     my_dict = {}

