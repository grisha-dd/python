final_list = []
i = 0
while True:
    user_input = input(
        "Выберете действие 'добавить товар','посмотреть структуру','вывести аналитику','завершить работу': ")
    if user_input == "добавить товар":
        i += 1
        input_list = [i]
        product_desc = {"название": "", "цена": 0, "количество": 0, "eд": ""}

        product_name = ""
        while product_name == "":
            product_name = input("Введите название товара: ")
            if product_name == "":
                print("Поле не может быть пустым.")

        product_price = -1
        while product_price < 0:
            input_price = input("Введите цену товара: ")
            if not input_price.strip("-").isnumeric():
                print("Поле не может быть текстом.Введите числовое значение.")
            elif float(input_price) < 0:
                print ("Поле не может быть отрицательным.Введите положительное число.")
            else:
                product_price=float(input_price)

        product_quantity = -1
        while product_quantity < 0:
            input_quantity = input("Введите доступное количество товара: ")
            if not input_quantity.strip("-").isnumeric():
                print("Поле не может быть текстом.Введите числовое значение.")
            elif float(input_quantity) < 0:
                print("Поле не может быть отрицательным.Введите положительное число.")
            else:
                product_quantity = float(input_quantity)

        product_unit = ""
        while product_unit == "":
            product_unit = input("Введите единицу измерения товара: ")
            if product_unit == "":
                print("Поле не может быть пустым.")

        product_desc["название"], product_desc["цена"], product_desc["количество"], product_desc[
            "eд"] = product_name, product_price, product_quantity, product_unit
        input_list.append(product_desc)
        final_list.append(tuple(input_list))
    elif user_input == "посмотреть структуру":
        print("Каталог пуст, добавьте товар") if len(final_list) == 0 else print(final_list)
    elif user_input == "вывести аналитику":
        if len(final_list) == 0:
            print("Каталог пуст, добавьте товар")
        else:
            list_names = []
            list_prices = []
            list_quantity = []
            list_unit = []
            for item in final_list:
                list_names.append(item[1]["название"])
                list_prices.append(item[1]["цена"])
                list_quantity.append(item[1]["количество"])
                list_unit.append(item[1]["eд"])
            analytics = {"название": list(set(list_names)), "цена": list(set(list_prices)),
                         "количество": list(set(list_quantity)), "eд": list(set(list_unit))}
            print(analytics)
    elif user_input == "завершить работу":
        break
    else:
        print("Неверная команда.")
