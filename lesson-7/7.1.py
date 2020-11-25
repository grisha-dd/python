# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц: 3 на 2, 3 на 3, 2 на 4. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

import sys


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([(4 * ' ').join(row) for row in self.matrix])

    def __add__(self, other):
        return Matrix([[str(int(self.matrix[rows][nums]) + int(other.matrix[rows][nums])) for nums in
                        range(len(self.matrix[rows]))] for rows in range(len(self.matrix))])

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)


try:
    q_matrix = int(input("Введите количество матриц: "))
except ValueError:
    sys.exit("Error. Введите действителное значение")
i = 0
all = []

try:
    rows = int(input("Введите количество рядов: "))
except ValueError:
    sys.exit("Error. Введите действителное значение")
try:
    columns = int(input("Введите количество столбцов : "))
except ValueError:
    sys.exit("Error. Введите действителное значение.")

while i < q_matrix:
    i += 1
    matrix = [input(f"Введите {columns} числа/чисел через пробел для формирования матрицы Nº{i}: ").split() for k in
              range(rows)]
    for k in matrix:
        for num in k:
            if not num.isdigit():
                sys.exit(f"Error. Введеные значения не действительны.")
        if len(k) != columns:
            sys.exit(f"Количество введенных чисел больше {columns}.")
    all.append(Matrix(matrix))

for index, m in enumerate(all):
    print(f"Матрица Nº{index + 1}:\n{m}")

print(f"Сумма матриц:\n{sum(all)}")
