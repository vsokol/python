# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
# где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
class Cell:
    def __init__(self, cnt):
        self.cnt = cnt

    def __add__(self, other):
        return Cell(self.cnt + other.cnt)

    def __sub__(self, other):
        if self.cnt >= other.cnt:
            return Cell(self.cnt - other.cnt)
        else:
            print("Нельзя большую клетку вычесть из меньшей")
            return None

    def __mul__(self, other):
        return Cell(self.cnt * other.cnt)

    def __floordiv__(self, other):
        return Cell(self.cnt // other.cnt)

    def __truediv__(self, other):
        return self // other

    def __str__(self):
        return f"{self.cnt}"

    def make_order(self, cell, count_cell_in_row):
        str_order = ""
        line = self.__gen_line(count_cell_in_row)
        for i in range(0, cell.cnt // count_cell_in_row):
            str_order += line + "\n"
        if cell.cnt % count_cell_in_row != 0:
            str_order += self.__gen_line(cell.cnt % count_cell_in_row)
        return str_order

    def __gen_line(self, len):
        """Генерация строки символов длиной len, состоящей из '*'"""
        return "".join(["*" for i in range(0, len)])


c_1 = Cell(5)
c_2 = Cell(2)
print(f"c_1 + c_2 = {c_1 + c_2}")
print(f"c_1 - c_2 = {c_1 - c_2}")
print(f"c_2 - c_1 = {c_2 - c_1}")
print(f"c_1 * c_2 = {c_1 * c_2}")
print(f"c_1 // c_2 = {c_1 // c_2}")
print(f"c_2 // c_1 = {c_2 // c_1}")
print(f"c_1 / c_2 = {c_1 / c_2}")
print(f"c_2 / c_1 = {c_2 / c_1}")

print(f"c_1.make_order(Cell(12), 5):")
print(f"{c_1.make_order(Cell(12), 5)}")
print(f"c_1.make_order(Cell(15), 5):")
print(f"{c_1.make_order(Cell(15), 5)}")
