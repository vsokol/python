# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, mt):
        self.mt = mt

    def __str__(self):
        max_len = self.__max_len() + 1
        string = ""
        for st in self.mt:
            for el in st:
                string += str(el).rjust(max_len)
            string += "\n"
        return string

    def __max_len(self):
        """ Определение длинны максимально длинного числа в матрице для форматирования"""
        max_len = 0
        for st in self.mt:
            for el in st:
                if max_len < len(str(el)):
                    max_len = len(str(el))
        return max_len

    def __add__(self, other):
        """Сложение матриц"""
        if self.dimension() != other.dimension():
            raise Exception("Несовпадение размерности матриц")

        list_matrix = []
        for i in range(len(self.mt)):
            list_st = []
            for j in range(len(self.mt[i])):
                list_st.append(self.mt[i][j] + other.mt[i][j])
            list_matrix.append(list_st)
        return Matrix(list_matrix)

    def dimension(self):
        """Определение размерности матриц"""
        # неполная проверка, так как внутри списка могут быть списки разных размеров
        # проверка только по кол-ву строк (кол-во вложенных списков) и длине первого списка
        dm_str = len(self.mt)
        if len(self.mt) != 0:
            dm_col = len(self.mt[0])
        else:
            dm_col = 0
        return dm_col, dm_str



mt_1 = Matrix([[1, 11, 111], [2, 22, 222]])
mt_2 = Matrix([[33, 333, 3], [44, 444, 4]])
print("Матрица: m_1")
print(mt_1)
print("Матрица: m_2")
print(mt_2)
mt_3 = mt_1 + mt_2
print("m_1 + m+2 = ")
print(mt_3)
