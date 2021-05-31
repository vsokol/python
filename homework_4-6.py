# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
from itertools import count, cycle

original_list = [i for i in range(10, 501, 10)]
print("original_list = {}".format(original_list))
for i in count(3):
    print("i = {}, original_list[i] = {}".format(i, original_list[i]))
    if i > 10:
        break

iterator = cycle(original_list)
for i in range(1, 20):
    print("i = {}, next(iterator) = {}".format(i, next(iterator)))