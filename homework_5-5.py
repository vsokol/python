# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce
from random import randint


def sm(prev_el, el):
    return prev_el + el


list_random_numbers = [randint(-1000, 1000) for el in range(20)]
str_numbers = " ".join(str(el) for el in list_random_numbers)
print(f"Сгенирированная последовательность числел: {str_numbers}")

file_name = "homework_5-5.txt"
with open(file_name, mode="w", encoding="utf-8") as f:
    f.write(str_numbers)

# подсчет суммы
with open(file_name, mode="r", encoding="utf-8") as f:
    data = [float(el) for el in f.read().split()]
print(f"Сумма всех чисел в файле = {reduce(sm, data)}")
