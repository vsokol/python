# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class InvalidDateFormat(Exception):

    def __init__(self, message):
        self.message = message


class Date:
    _MIN_YEAR = 1
    _MAX_YEAR = 9999
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, date):
        self.date = date

    @classmethod
    def get_date(cls, date):
        date_str = str(date)
        list_date = date_str.split("-")
        if (len(date_str) != 10) or (len(list_date) != 3):
            raise InvalidDateFormat("Длина строки с датой должна быть равны 10. Формат - 'dd-mm-yyyy'")
        try:
            year = int(list_date[2])
            month = int(list_date[1])
            day = int(list_date[0])
        except ValueError:
            raise InvalidDateFormat("Неверный формат даты. Формат - 'dd-mm-yyyy'")
        return year, month, day

    @staticmethod
    def check_date(year, month, day):
        if not Date._MIN_YEAR <= year <= Date._MAX_YEAR:
            raise ValueError(f"Год должен находится в интервале от {Date._MIN_YEAR} до {Date._MAX_YEAR}", year)
        if not 1 <= month <= 12:
            raise ValueError('Месяц должен находиться в интервале от 1 до 12', month)
        dim = Date._days_in_month(year, month)
        if not 1 <= day <= dim:
            raise ValueError(f"День должен находиться в интервале от 1 до {dim}", day)
        return True

    @staticmethod
    def _days_in_month(year, month):
        "year, month -> определение кол-ва дней в месяце"
        assert 1 <= month <= 12, month
        if month == 2 and Date._is_leap(year):
            return 29
        return Date._DAYS_IN_MONTH[month]

    @staticmethod
    def _is_leap(year):
        "year -> 1 если год високосный, иначе 0"
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year, month, day = Date.get_date("25-05-2021")
print(f"year = {year}, month = {month}, day = {day}")
print(Date.check_date(year, month, day))

year, month, day = Date.get_date("20-06-1800")
print(f"year = {year}, month = {month}, day = {day}")
print(Date.check_date(year, month, day))

year, month, day = Date.get_date("29-02-2020")
print(f"year = {year}, month = {month}, day = {day}")
print(Date.check_date(year, month, day))

year, month, day = Date.get_date("29-02-2021")
print(f"year = {year}, month = {month}, day = {day}")
print(Date.check_date(year, month, day))

