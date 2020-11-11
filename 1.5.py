

sales = int(input("Введите прибыль Вашей фирмы: "))
cost = int(input("Введите издержки Вашей фирмы: "))

margin = sales - cost

if margin > 0:
    print("Результат: Прибыль")
    print("Pентабельность:", margin/sales)
    employees = int(input("Введите численность сотрудников Вашей фирмы: "))
    print("Прибыль фирмы в расчете на одного сотрудника:", int(margin/employees))
else:
    print("Результат: Убыток")