#подглядел в телеге(
a = list(input('введите список через запятую'))

for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(a)