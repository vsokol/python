# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость атомобиля {self.name} = {self.speed}")


class TownCar(Car):
    _limit = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        dif = self.speed - self._limit
        if dif > 0:
            print(
                f"Машина {self.name} превыслила допустимую скорость на {dif} км/ч (допустимая скорость {self._limit} км/ч)")
        else:
            super().show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(TownCar):
    _limit = 40


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = Car(80, "Красный", "Запорожец", False)
car_1.go()
car_1.turn("налево")
car_1.show_speed()
car_1.stop()

town_car_1 = TownCar(70, "Желтый", "Москвич")
town_car_1.show_speed()
town_car_2 = TownCar(30, "Желтые", "Жигули")
town_car_2.show_speed()

work_car_1 = WorkCar(30, "Серый", "Краз")
work_car_1.show_speed()
work_car_2 = WorkCar(90, "Зеленый", "Камаз")
work_car_2.show_speed()