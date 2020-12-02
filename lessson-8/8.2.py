# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    pass


class NotDigitErr(OwnError):
    pass


class CantDivideByZeroErr(OwnError):
    pass


def notstangenumber(param):
    check = param
    if check.startswith("-"):
        check = check[1:]
    check = check.split(".")
    if len(check) > 2 or not check[0].isnumeric() or (len(check) == 2 and not check[1].isnumeric()):
        raise NotDigitErr


try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    notstangenumber(a)
    notstangenumber(b)
    if b == "0":
        raise CantDivideByZeroErr
except NotDigitErr:
    print("Error. Введите действительные значения.")
except CantDivideByZeroErr:
    print("Error. На 0 делить нельзя.")
else:
    print(float(a) / float(b))
