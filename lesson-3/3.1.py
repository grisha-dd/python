# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def my_sub(arg_1, arg_2):
    return arg_1 / arg_2


while True:
    try:
        arg_1 = float(input("Enter the first number: "))
        arg_2 = float(input("Enter the second number: "))
        print(my_sub(arg_1, arg_2))
    except ZeroDivisionError:
        print("Oh no... You can´t divide by 0.")
