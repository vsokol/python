# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
def exponentiation_1(x, y):
    return x ** y


def exponentiation_2(x, y):
    pw = 1
    for i in range(abs(y)):
        pw *= x
    return 1 / pw


def check_input_data(str_x, str_y):
    try:
        x = float(str_x)
        if x <= 0:
            return False, str_x + "не является действительным положительным числом", None
    except ValueError:
        return False, str_x + " не является действительным числом", None
    try:
        y = int(str_y)
        if y >= 0:
            return False, str_y + "не является целым отрицательным числом", None
    except ValueError:
        return False, str_y + " не является целым числом", None
    return True, x, y


str_x = input("Введите основание (действительное положительное число): ")
str_y = input("Введите степень (целое отрицательное число): ")
res, x, y = check_input_data(str_x, str_y)
if res:
    pw_1 = exponentiation_1(x, y)
    pw_2 = exponentiation_2(x, y)
    print("exponentiation_1({}, {}) = {}".format(x, y, pw_1))
    print("exponentiation_2({}, {}) = {}".format(x, y, pw_2))
else:
    print(x)
