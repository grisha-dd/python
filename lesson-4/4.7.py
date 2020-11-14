# from math import factorial

n = int(input("Enter any number: "))


def my_factorial(i):
    if i == 0:
        return 1
    return my_factorial(i - 1) * i


def fact(n):
    for el in range(0, n + 1):
        # yield factorial(el)
        yield el, my_factorial(el)


for num_n, factorial_n in fact(n):
    print(f"Факториал {num_n}! = {factorial_n}")
