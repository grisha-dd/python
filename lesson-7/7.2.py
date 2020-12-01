# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет расхода
# ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
# проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
import sys


class Clothes(ABC):
    def __init__(self, title, value):
        self._title = title
        self.value = value
        # self.title = title

    @property
    def value(self):
        return self._value

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, value, title="Пальто"):
        self.title = title
        super().__init__(self, value)

    @Clothes.value.setter
    def value(self, value):
        if value < 34:
            self._value = 34
        elif value > 86:
            self._value = 86
        elif value % 2 != 0:
            self._value = value + 1
        else:
            self._value = value

    def fabric_consumption(self):
        return round(self.value / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, value, title="Костюмa"):
        self.title = title
        super().__init__(self, value)

    @Clothes.value.setter
    def value(self, value):
        if value < 110:
            self._value = 110
        elif value > 240:
            self._value = 240
        else:
            self._value = value

    def fabric_consumption(self):
        return round(((2 * self.value + 0.3) / 100), 2)


choice = input("Введите 1-2 для выбора типа одежды для рассчета расхода ткани:\n1.Пальто\n2.Костюм\nВаш выбор: ")
if choice == "1":
    try:
        v_choice = int(input("Введите размер от 34 до 86: "))
        final_prod = Coat(v_choice)
    except ValueError:
        sys.exit(f"Введенное значение не действительно.")
elif choice == "2":
    try:
        v_choice = int(input("Введите рост от 110 до 240: "))
        final_prod = Suit(v_choice)
    except ValueError:
        sys.exit(f"Введенное значение не действительно.")
else:
    sys.exit(f"Введенное значение не действительно.")
print(
    f"Расход ткани для производства {final_prod.title.lower()} для {'размера' if choice == '1' else 'роста'} {final_prod.value}: {final_prod.fabric_consumption()} м")
