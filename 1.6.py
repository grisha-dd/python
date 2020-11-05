result = 0
while result <= 0:
    a = int(input("Введите параметр a: "))
    b = int(input("Введите параметр b: "))
    if a < 0 or b < 0:
        print("Оба параметра должы быть положительным числом.")
    elif b < a:
        print("Параметр b должен быть больше или равен параметру a.")
    else:
        result = 1
        while a < b:
            a = a * 1.1
            result += 1
print(result)
