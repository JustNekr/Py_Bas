from googletrans import Translator

translator = Translator()
with open("text_4.txt", 'r', encoding='utf-8') as file:
    with open("new_text.txt", "w", encoding='utf-8') as file2:
        for line in file:
            print(translator.translate(line, dest='ru').text, file=file2)
