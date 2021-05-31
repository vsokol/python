# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def input_number(num):
    str_num = input("Введите {} число: ".format(num))
    res = False
    nm = 0
    if str_num.isdigit():
        nm = int(str_num)
        res = True
    else:
        print("Число {} не является числом".format(str_num))
    return res, nm


res, num_1 = input_number(1)
if not res:
    exit()
res, num_2 = input_number(2)
if not res:
    exit()


def division(var_1, var_2):
    try:
        return True, var_1 / var_2
    except ZeroDivisionError:
        return False, 0


res, dv = division(num_1, num_2)
if res:
    print("{} / {} = {}".format(num_1, num_2, dv))
else:
    print("Ошибка при выполение деления числа {} на число {}".format(num_1, num_2))
