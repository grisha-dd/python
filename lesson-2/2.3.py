# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

month_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август",
                "сентябрь", "октябрь", "ноябрь", "декабрь"]
seasons_dict = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето",
                9: "осень", 10: "осень", 11: "осень", 12: "зима"}
num_month = ""
while True:
    num_month = input("Введите номер месяца от 1 до 12: ")
    if num_month.isdigit() and int(num_month) >= 1 and int(num_month) <= 12:
        break
    print("Error. Введенное значение не действительно")

user_season  = seasons_dict.get(int(num_month))
user_month = month_list [int(num_month)-1]
print ("Месяц: ", user_month,", ", "время года: ", user_season, sep="")