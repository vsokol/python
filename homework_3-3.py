# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def sum_max_two(var_1, var_2, var_3):
    try:
        lst = [var_1, var_2, var_3]
        mx_1 = max(lst)
        lst.remove(mx_1)
        mx_2 = max(lst)
        return True, mx_1 + mx_2
    except TypeError:
        return False, "Должны быть только числа"

var_1 = 1
var_2 = 1.1
var_3 = 4
res, sm = sum_max_two(var_1, var_2, var_3)
if res:
    print("Сумма двух наибольших аргументов = {}".format(sm))
else:
    print("Ошибка. {}".format(sm))
