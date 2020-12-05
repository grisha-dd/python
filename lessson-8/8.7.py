# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"{self.a}+{self.b}j"

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


com_1 = ComplexNum(4, 5)
com_2 = ComplexNum(6, 10)

print(f"Complex number 1: {com_1}")
print(f"Complex number 2: {com_2}")

print(f"{com_1} + {com_2} = {com_1+com_2}")
print(f"{com_1} * {com_2} = {com_1*com_2}")
