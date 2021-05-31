# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом
# проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def get_tissue_consumption(self):
        pass

    @property
    @abstractmethod
    def get_all_tissue_consumption(self):
        pass


class Coat(Clothes):
    __consumption = 0

    def __init__(self, v):
        self.v = v
        Coat.__consumption += self.get_tissue_consumption()

    def get_tissue_consumption(self):
        return self.v / 6.5 + 0.5

    @property
    def get_all_tissue_consumption(self):
        return Coat.__consumption


class Suit(Clothes):
    __consumption = 0

    def __init__(self, h):
        self.h = h
        Suit.__consumption += self.get_tissue_consumption()

    def get_tissue_consumption(self):
        return self. \
                   h * 2 + 0.3

    @property
    def get_all_tissue_consumption(self):
        return Suit.__consumption


c_1 = Coat(13)
c_2 = Coat(26)
s_1 = Suit(10)
s_2 = Suit(20)
print(f"Расход ткани на пальто c_1 = {c_1.get_tissue_consumption()}, на пальто c_2 = {c_2.get_tissue_consumption()}")
print(f"Расход ткани на все пальто {c_1.get_all_tissue_consumption}")
print(f"Расход ткани на костюм s_1 = {s_1.get_tissue_consumption()}, на костюм s_2 = {s_2.get_tissue_consumption()}")
print(f"Расход ткани на все костюмы {s_2.get_all_tissue_consumption}")
print("--------------------------------------------------------------------------------------------------------------")
print(f"Расход ткани на всю одежду = {c_1.get_all_tissue_consumption + s_1.get_all_tissue_consumption}")
