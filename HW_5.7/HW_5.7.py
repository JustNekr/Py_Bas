import json

with open('text_7.txt', 'r', encoding="utf-8") as file:
    with open('new_text.json', 'w', encoding="utf-8") as j_file:
        my_dict = {line.split()[0]: (float(line.split()[2]) - float(line.split()[3])) for line in file}
        print(my_dict)
        average = sum([i for i in my_dict.values() if i > 0]) / len([i for i in my_dict.values() if i > 0])
        print(average)
        my_list = (my_dict, {"average_profit": average})
        json.dump(my_list, j_file, ensure_ascii=False, indent=4)
