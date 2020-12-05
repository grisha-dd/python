# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
# валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
# данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def dates_to_nums(cls, data):
        day, month, year = map(int, data.split("/"))
        print(f"Day: {day}. Month: {month}. Year: {year}")

    @staticmethod
    def check_dates(data):
        dates = data.split("/")
        month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if not 0 < int(dates[2]) < 3000:
            print("Year is not valid.")
        if not 0 < int(dates[1]) <= 12:
            print("Month is not valid.")
        elif not 0 < int(dates[0]) <= month_dict.get(int(dates[1])):
            print(f"Day is not valid. Month {dates[1]} doesn't have {dates[0]} day(s)")

try:
    data_1 = input("Введите дату в формате ДД/ММ/ГГГГ: ")
    Data.dates_to_nums(data_1)
    Data.check_dates(data_1)
except ValueError:
    print("Введеный формат не верен.")



