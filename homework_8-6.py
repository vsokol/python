# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
import copy
from abc import ABC, abstractmethod


class InvalidWarehouse(Exception):

    def __init__(self, message):
        self.message = message


class Warehouse:
    _number_of_occupied_places = 0
    _list_of_equipment = dict()

    def __init__(self, capacity, list_of_equipment):
        Warehouse._check_attr_capacity(capacity)
        Warehouse._check_attr_list_of_equipment(list_of_equipment)
        w_capacity = capacity
        w_list_of_equipment = copy.deepcopy(list_of_equipment)
        self._check_capacity(w_capacity, w_list_of_equipment)
        self._capacity = w_capacity
        self._list_of_equipment = w_list_of_equipment
        self._number_of_occupied_places = sum(self._list_of_equipment.values())

    @staticmethod
    def _check_attr_capacity(capacity):
        if not isinstance(capacity, int):
            raise InvalidWarehouse("Атрибут capacity должен быть типа int")

    @staticmethod
    def _check_attr_list_of_equipment(list_of_equipment):
        if not isinstance(list_of_equipment, dict):
            raise InvalidWarehouse(f"Параметра list_of_equipment должен быть словарем")
        for key, value in list_of_equipment.items():
            if not isinstance(key, OfficeEquipment):
                raise InvalidWarehouse(f"Объект {key} не является потомком OfficeEquipment")
            if not isinstance(value, int):
                raise InvalidWarehouse(f"Неверный тип, указывающий кол-во техники для {key}. Должен быть int.")

    def _check_capacity(self, capacity, list_of_equipment):
        num = sum(self._list_of_equipment.values()) + sum(list_of_equipment.values())
        cp = capacity if capacity is not None else self._capacity
        if num > cp:
            raise InvalidWarehouse(f"Не хватает емкости склада для размещения всей техники. "
                                   f"Емкость склада = {cp}, кол-во техники = {num}")

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
        self._check_attr_capacity(value)
        self._check_capacity(value, dict())
        self._capacity = value

    @property
    def number_of_occupied_places(self):
        return self._number_of_occupied_places

    @number_of_occupied_places.getter
    def number_of_occupied_places(self):
        return self._number_of_occupied_places

    @property
    def list_of_equipment(self):
        return self._list_of_equipment

    @list_of_equipment.getter
    def list_of_equipment(self):
        return self._list_of_equipment

    def _add_equipment(self, equipment, count):
        vl = self._list_of_equipment.get(equipment)
        if vl is not None:
            self._list_of_equipment.update({equipment: vl + count})
        else:
            self._list_of_equipment.update({equipment: count})
        self._number_of_occupied_places += count

    def _remove_equipment(self, equipment, count):
        vl = self._list_of_equipment.get(equipment)
        if vl is None:
            raise InvalidWarehouse(f"{equipment} на складе нет")
        else:
            if count > vl:
                self._list_of_equipment.update({equipment: 0})
                self._number_of_occupied_places -= vl
                raise InvalidWarehouse(
                    f"На складе недостаточно {equipment}. Запрошено {count}, доступно {vl}. Будет списано {vl}")
            else:
                self._list_of_equipment.update({equipment: count})
                self._number_of_occupied_places -= count

    def acceptance(self, list_of_equipment):
        Warehouse._check_attr_list_of_equipment(list_of_equipment)
        self._check_capacity(None, list_of_equipment)
        for k, v in list_of_equipment.items():
            self._add_equipment(k, v)

    def consumption(self, list_of_equipment):
        Warehouse._check_attr_list_of_equipment(list_of_equipment)
        for k, v in list_of_equipment.items():
            self._remove_equipment(k, v)


class OfficeEquipment(ABC):
    def __init__(self, name, kind, height, width, length, weight):
        self.name = name
        self.kind = kind
        self.height = height
        self.width = width
        self.length = length
        self.weight = weight

    def __repr__(self) -> str:
        return f"{self.kind} {self.name}, {self.height}x{self.width}x{self.length}, {self.weight} кг."

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

    def __hash__(self) -> int:
        return hash((self.name, self.height, self.width, self.length, self.weight, self.print_speed, self.is_color))

    def __eq__(self, o: object) -> bool:
        return (isinstance(o, type(self))
                and (self.name, self.height, self.width, self.length, self.weight, self.print_speed, self.is_color) ==
                (o.name, o.height, o.width, o.length, o.weight, o.print_speed, o.is_color))


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

    def __hash__(self) -> int:
        return hash(
            (self.name, self.height, self.width, self.length, self.weight, self.resolution_x, self.resolution_y))

    def __eq__(self, o: object) -> bool:
        return (isinstance(o, type(self))
                and (
                    self.name, self.height, self.width, self.length, self.weight, self.resolution_x,
                    self.resolution_y) ==
                (o.name, o.height, o.width, o.length, o.weight, o.resolution_x, o.resolution_y))


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

    def __hash__(self) -> int:
        return hash((self.name, self.height, self.width, self.length, self.weight, self.is_double_sided_copy))

    def __eq__(self, o: object) -> bool:
        return (isinstance(o, type(self))
                and (self.name, self.height, self.width, self.length, self.weight, self.is_double_sided_copy) ==
                (o.name, o.height, o.width, o.length, o.weight, o.is_double_sided_copy))


equipment_dict = {Printer("Epson XP-600", 14, 39, 34, 5, 12, True): 3,
                  Scanner("Canon CanoScan LiDE 300", 5, 25, 37, 2, 2400, 2400): 2,
                  Xerox("AltaLink C8130", 62, 72, 113, 143, True): 1}
warehouse = Warehouse(20, equipment_dict)
print(f"warehouse = {warehouse}")
print("-- поступление на склад")
warehouse.acceptance(
    {Printer("Epson XP-600", 14, 39, 34, 5, 12, True): 3, Scanner("Canon CanoScan", 5, 25, 37, 2, 2400, 2400): 2})
print(f"warehouse = {warehouse}")
print(warehouse.list_of_equipment)
print("-- списание со склада")
warehouse.consumption(
    {Printer("Epson XP-600", 14, 39, 34, 5, 12, True): 3, Scanner("Canon CanoScan", 5, 25, 37, 2, 2400, 2400): 2})
print(warehouse.list_of_equipment)
print(f"warehouse = {warehouse}")
