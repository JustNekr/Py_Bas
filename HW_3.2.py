def man_data(**kwargs):
    """я так понял 'вывод одной строкой' """
    return ' '.join(kwargs.values())


print(
    man_data(name=input('введите имя '), surname=input('введите фамилию '), birth_date=input('введите дату рождения '),
             city=input('введите город проживания '), email=input('введите email '), phone=input('введите телефон ')))
