my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(my_list) if el > my_list[i - 1] and i!=0]
# вместо  i!=0 можно было (i-1)>0
print(my_list)
print(new_list)
