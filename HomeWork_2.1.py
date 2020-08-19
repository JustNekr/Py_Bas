my_list = [2, 3.43, (5 + 6j), 'строка', [1, 2, 3], ("кортеж", 23, True), {'a', 'k', 'b', 'd', 'r'},
           frozenset({'a', 'k', 'b', 'd', 'r'}), {'key_1': 'val_1', 'key_2': 'val_2'}, True, False, (b"some text"),
           bytearray(b"some text"), None]
for el in my_list:
    print(type(el))
