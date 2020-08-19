products = []
i = 0
n = int(input('сколько товаров вы хотите внести: '))

while i < n:
    products.append(i)
    i += 1

for i, el in enumerate(products):
    products_dict = {}
    name_dict = {"название": input('Введите название тоовара: ')}
    price_dict = {'цена': input('Введите цену тоовара: ')}
    amount_dict = {'количество': input('Введите количество тоовара: ')}
    unit_dict = {'ед': input('Введите единицу измерения тоовара: ')}
    products_dict.update(name_dict)
    products_dict.update(price_dict)
    products_dict.update(amount_dict)
    products_dict.update(unit_dict)
    products[i] = (i + 1, products_dict)

print(products)

name_list = []
price_list = []
amount_list = []
unit_list = []
for i in products:
    name_list.append(i[1].get('название'))
    price_list.append(i[1].get('цена'))
    amount_list.append(i[1].get('количество'))
    unit_list.append(i[1].get('ед'))
products_dict = {}
products_dict.update({'название': name_list})
products_dict.update({'цена': price_list})
products_dict.update({'количество': amount_list})
products_dict.update({'ед': unit_list})
print(products_dict)
