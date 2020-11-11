# Решение 1

# def my_func():
#     x = int(input("Введите положительное число: "))
#     y = int(input("Введите целое отрицательное число: "))
#     return x ** y
#
#
# print(my_func())


# Решение 2

def my_func():

    x = int(input("Введите положительное число: "))
    if x <= 0:
        return "Error. Число должно быть положительным"
    y = abs(int(input("Введите целое отрицательное число: ")))
    if x >= 0:
        return "Error. Число должно быть целым отрицательным"
    i = 2
    result = x
    while i <= y:
        result = result * x
        i += 1
    return 1/result


print(my_func())
