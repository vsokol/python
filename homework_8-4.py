# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
from abc import ABC, abstractmethod


class Warehouse:

    def __init__(self, capacity, number_of_occupied_places=0):
        self._capacity = int(capacity)
        self._number_of_occupied_places = int(number_of_occupied_places)

    def __str__(self) -> str:
        return f"Емкость склада - {self._capacity}, свободных мест - {self._capacity - self._number_of_occupied_places}"

    @property
    def capacity(self):
        return self._capacity

    @capacity.getter
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = int(value)


class OfficeEquipment(ABC):
    def __init__(self, name, kind, height, width, length, weight):
        self.name = name
        self.kind = kind
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def __str__(self) -> str:
        return f"Название - {self.name}, тип - {self.kind}, габариты (в сантиметрах) - {self.height}x{self.width}x{self.length}, масса - {self.weight} кг."

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Printer(OfficeEquipment):
    def __init__(self, name, height, width, length, weight, print_speed, is_color):
        super().__init__(name, "Printer", height, width, length, weight)
        self.print_speed = print_speed
        self.is_color = is_color

    def start(self):
        return "Печать запущена..."

    def stop(self):
        return "Печать остановлена..."

    def __str__(self) -> str:
        return super().__str__() + f", скорость печати - {self.print_speed} листов в минуту, цветная печать - {'Да' if self.is_color else 'Нет'}"


class Scanner(OfficeEquipment):
    def __init__(self, name, height, width, length, weight, resolution_x, resolution_y):
        super().__init__(name, "Scanner", height, width, length, weight)
        self.resolution_x = resolution_x
        self.resolution_y = resolution_y

    def start(self):
        return "Сканирование запущено..."

    def stop(self):
        return "Сканирование остановлено..."

    def __str__(self) -> str:
        return super().__str__() + f", разрешение {self.resolution_x}x{self.resolution_y}"


class Xerox(OfficeEquipment):
    def __init__(self, name, height, width, length, weight, is_double_sided_copy):
        super().__init__(name, "Scanner", height, width, length, weight)
        self.is_double_sided_copy = is_double_sided_copy

    def start(self):
        return "Ксерокопирование запущено..."

    def stop(self):
        return "Ксерокопирование остановлено..."

    def __str__(self) -> str:
        return super().__str__() + f", двухстороннее ксерокопирование - {'Да' if self.is_double_sided_copy else 'Нет'}"


printer_1 = Printer("Epson XP-600", 14, 39, 34, 5, 12, True)
scanner_1 = Scanner("Canon CanoScan LiDE 300", 5, 25, 37, 2, 2400, 2400)
xerox_1 = Xerox("AltaLink C8130", 62, 72, 113, 143, True)
print(printer_1)
print(scanner_1)
print(xerox_1)

warehouse = Warehouse(100, 25)
print(f"warehouse = {warehouse}")
warehouse.capacity = 120
print(f"warehouse.get_capacity() - {warehouse.capacity}")
