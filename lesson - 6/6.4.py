# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево).  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
from random import choice
from termcolor import cprint, colored
from math import inf


class Car:
    def __init__(self, speed, color, car_name, is_police, limit):
        self.speed = speed
        self.color = color
        self.name = car_name
        self.is_police = is_police
        self.limit = limit

    def go(self):
        return "Врум-врум! Машина поехала"

    def stop(self):
        return "Машина остановилась."

    def turn(self):
        return choice(["Едем влево", "Едем вправо", "Едем прямо", "Едем назад"])

    def show_speed(self):
        return f" со скорость {self.speed} км/ч."


class TownCar(Car):
    def __init__(self, speed, color, car_name):
        super().__init__(speed, color, car_name, False, 60)

    def show_speed(self):
        if self.speed > self.limit:
            return f". Превышении скорости на {self.speed - self.limit} км/ч."
        else:
            return f" со скорость {self.speed} км/ч."


class SportCar(Car):
    def __init__(self, speed, color, car_name):
        super().__init__(speed, color, car_name, False, inf)


class WorkCar(Car):
    def __init__(self, speed, color, car_name):
        super().__init__(speed, color, car_name, False, 40)

    def show_speed(self):
        if self.speed > self.limit:
            return f". Превышении скорости на {self.speed - self.limit} км/ч."
        else:
            return f" со скорость {self.speed} км/ч."


class PoliceCar(Car):
    def __init__(self, speed, color, car_name):
        super().__init__(speed, color, car_name, True, inf)


cars = {1: TownCar, 2: SportCar, 3: WorkCar, 4: PoliceCar}
name = {1: "Седан", 2: "Спорткар", 3: "Грузовик", 4: "Полицейский автомобиль"}
colors = {1: "Черный", 2: "Белый", 3: "Желтый", 4: "Красный", 5: "Зеленый", 6: "Синий"}

while True:
    choose_car = input("Выберите машину, введите 1-4:\n1. Седан\n2. Спорткар\n3. Грузовик\n4. Полиция\nВаш выбор: ")
    if choose_car.isdigit() and 1 <= int(choose_car) <= 4:
        choose_car = int(choose_car)
        break
    else:
        print("Введенное значение не действительно")

while True:
    choose_color = input("Выберите цвет машины, введите 1-6:\n1. Черный\n2. Белый\n3. Желтый\n4. Красный\n5. "
                         "Зеленый\n6. Синий\nВаш выбор: ")
    if choose_color.isdigit() and 1 <= int(choose_color) <= 6:
        choose_color = int(choose_color)
        break
    else:
        print("Введенное значение не действительно")

while True:
    choose_speed = input("Введите скорость машины в км/ч: ")
    if choose_speed.isdigit() and float(choose_speed) > 0:
        choose_speed = float(choose_speed)
        break
    else:
        print("Введенное значение не действительно")

final_car = cars[choose_car](choose_speed, colors[choose_color], name[choose_car])

cprint(f"Ваша машина: {final_car.color} {final_car.name.lower()}.", "grey", "on_white", attrs=['bold'])
cprint(f"{final_car.go()}{final_car.show_speed()}", "grey", "on_white", attrs=['bold'])

if float(final_car.speed) > float(final_car.limit):
    while True:
        change_speed = input("Хотите снизить скорость\n1. Да\n2. Нет\nВаш выбор: ")
        if change_speed.isdigit() and int(change_speed) == 1:
            final_car = cars[choose_car](final_car.limit, colors[choose_color], name[choose_car])
            print(f"Скорость снижена до {final_car.limit} км/ч.")
            break
        if change_speed.isdigit() and int(change_speed) == 2:
            print(f"Упс... {colored(final_car.stop(),'grey', 'on_white', attrs=['bold'])}\nВас остановила полиция и "
                  f"забрала машину на штраф стоянку.\nПрограмма завершена.")
            break
        else:
            print("Введенное значение не действительно")

if float(final_car.speed) <= float(final_car.limit):
    while True:
        actions = {1: final_car.turn, 2: final_car.stop, 3: final_car.go}
        action = input("Выберите действие, введите 1-2 или нажмите q для выхода:\n1.Поменять "
                       "направление\n2.Остановить машину\nВаш выбор: ")
        if action.isdigit() and int(action) == 1:
            cprint(actions[int(action)](), "grey", "on_white", attrs=['bold'])
        elif action.isdigit() and int(action) == 2:
            cprint(actions[int(action)](), "grey", "on_white", attrs=['bold'])
            action = input(
                "Хотите поехать снова?\n1. Да.\n2. Нет, закончить программу\nВаш выбор: ")
            if action.isdigit() and int(action) == 1:
                cprint(actions[int(action)](), "grey", "on_white", attrs=['bold'])
            elif action.isdigit() and int(action) == 2 or action == "q":
                print("Программа завершена")
                break
            else:
                print("Введенное значение не действительно")
        elif action == "q":
            print("Программа завершена")
            break
        else:
            print("Введенное значение не действительно")
