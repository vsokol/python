# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open("homework_5-1.py", mode="r", encoding="utf-8") as f:
    count_lines = 0
    count_words = 0
    for line in f:
        count_lines += 1
        words = line.split()
        count_words += len(words)
print("Кол-во строк = {}".format(count_lines))
print("Кол-во слов = {}".format(count_words))
