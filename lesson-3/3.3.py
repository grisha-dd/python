# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(arg_1, arg_2, arg_3):
    func_list = [arg_1, arg_2, arg_3]
    func_list.remove(min(func_list))
    return sum(func_list)


print(my_func(int(input("Enter first number: ")), int(input("Enter second number: ")),
              int(input("Enter third number: "))))
