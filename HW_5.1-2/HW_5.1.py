import sys
import os

try:
    with open("text_1.txt", "x+", encoding="utf-8") as file:
        while True:
            text = input('input some data: ')
            if text == '':
                break
            else:
                file.write(f'{text}\n')
except IOError:
    print('!!!ERROR!!!\nFile already exists!!!')

with open("text_1.txt", "r", encoding='utf-8') as file:
    c = 1
    for i in file:
        print(f"В строке № {c} : {len(i.split())} слов")
        c += 1
print(f"Всего строк в файле {c - 1}")
