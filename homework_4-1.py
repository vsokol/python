# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv


def salary(working, rate, bonus):
    try:
        return float(working) * float(rate) + float(bonus)
    except ValueError:
        print("Параметры дожлжны быть числовыми")

try:
    working = argv[1]
    rate = argv[2]
    bonus = argv[3]
    print(salary(argv[1], argv[2], argv[3]))
except IndexError:
    print("Недостаточно параметров для скрипта. Должно быть 3.")


