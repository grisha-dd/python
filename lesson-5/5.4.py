# Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
from googletrans import Translator
translator = Translator()


with open("text_4.txt", "r", encoding="utf-8") as original:
    for line in original:
        with open("text_4_trans_ru_dd.txt", "a", encoding="utf-8") as trans_ru:
            result = translator.translate(line, dest="ru")
            print(result.text)
            trans_ru.write(f"{result.text}\n")
