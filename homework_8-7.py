# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}{"+" if self.y >= 0 else ""}{self.y}j)'

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x*other.x - self.y*other.y, self.x*other.y + self.y*other.x)


c_1 = Complex(1, 3)
c_2 = Complex(2, -3)
c_3 = Complex(-4, 7)
print(f"c_1 = {c_1}")
print(f"c_2 = {c_2}")
print(f"c_3 = {c_3}")
print(f"c_1 + c_2 = {c_1 + c_2}")
print(f"c_1 + c_2 + c_3 = {c_1 + c_2 + c_3}")
print(f"c_1 * c_2 = {c_1 * c_2}")
print(f"c_1 * c_3 = {c_1 * c_3}")
print(f"c_1 * c_2 * c_3 = {c_1 * c_2 * c_3}")
