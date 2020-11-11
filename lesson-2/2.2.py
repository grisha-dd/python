# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1,
# 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
# необходимо использовать функцию input().

while True:
    user_input = input("Вы хотите ввести значения по очереди или целым списком? Введите separate или list: ")
    list = []
    if user_input == "list":
        list = input("Введите список через запятую: ").split(",")
    elif user_input == "separate":
        while True:
            check = input("Введите элеменит или 'stop' для окончания: ")
            if check == "stop":
                break
            list.append(check)
    else:
        print("Error. Введите separate или list: ")
        continue
    i = 0
    for el in range(len(list) // 2):
        list[i], list[i + 1] = list[i + 1], list[i]
        i += 2
    print(list)
