# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def list_multiplication(prev_el, el):
    return prev_el * el


print("multiplication = {}".format(reduce(list_multiplication, [i for i in range(100, 10001) if i % 2 == 0])))

