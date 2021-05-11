# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
file_name_read = "text_4.txt"
file_name_write = "text_4-1.txt"
try:
    dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    with open(file_name_read, mode="r", encoding="utf-8") as f_read, open(file_name_write, mode="w", encoding="utf-8") as f_write:
        for line in f_read:
            words = line.split()
            line_write = ""
            for i in range(len(words)):
                if dict.get(words[i]) is not None:
                    words[i] = dict.get(words[i])
            f_write.write(" ".join(words) + "\n")
except FileNotFoundError:
    print(f"Не найден файл '{file_name_read}'")
