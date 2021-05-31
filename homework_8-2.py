# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.
class ErrorDivisionByZero(Exception):

    def __init__(self, message):
        self.message = message


while True:
    numerator = input("Введите числитель: ")
    denominator = input("Введите знаменатель (для выхода нажмите Enter: ")
    if denominator == "":
        break
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        print(f"Или числитель {numerator} или знаменатель {denominator} не являются числом. Повторите ввод данных")

    try:
        if denominator == 0:
            raise ErrorDivisionByZero("На 0 делить нельзя")
        print(f"{numerator} / {denominator} = {numerator / denominator}")
    except ErrorDivisionByZero:
        print(f"Знаменатель {denominator} равен 0. На 0 делить нельзя. Повторите ввод данных")