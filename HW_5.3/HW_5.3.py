try:
    with open("text_3.txt", "r", encoding="utf-8") as file:
        c = 0
        i = 0
        print("Менее 20000 зарабатывают:")
        for line in file:
            if float(line.split()[1]) < 20000:
                print(line.split()[0])
                c += float(line.split()[1])
                i += 1
            else:
                c += float(line.split()[1])
                i += 1
    print(f"Средняя ЗП составляет: {c / i}")
except IOError:
    print('!!!ERROR!!!')
