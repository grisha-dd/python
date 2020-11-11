def my_sum():
    total_sum = 0
    while True:
        user_str = input("Введите строку чисел, разделенных пробелом. Для выхода введите z: ")
        user_list = user_str.split(" ")
        sub_sum = 0

        for item in user_list:
            if item == "z":
                return sub_sum, total_sum
            sub_sum += int(item)
            total_sum += int(item)
        print(f"Промежуточная сумма: {sub_sum}. Общая сумма: {total_sum}")


sub_sum_val, total_sum_val = my_sum()
print(f"Промежуточная сумма: {sub_sum_val}. Общая сумма: {total_sum_val}")
print("Программа завершена")
