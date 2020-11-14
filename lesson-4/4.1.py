# C:\Users\Grisha\Desktop\data-science\Python\python_repo\lesson-4>
# 4.1.py 30000 12 500 90
from sys import argv

script_name, year_salary, year_pays, month_bonus, bonus_percentage = argv
year_salary, year_pays, month_bonus, bonus_percentage = float(year_salary), int(year_pays), float(month_bonus), float(
    bonus_percentage)

if year_salary < 0 or not (year_pays == 12 or year_pays == 14) or month_bonus < 0 or (0 > bonus_percentage > 100):
    print("Введите дейсвительные значения через пробел. Годовая зарплата, количество годовых платежей (12 или 14), "
          "месячный бонус, процент выполнения плана (от 0 до 100). ")
else:
    gross_salary = float(year_salary / year_pays + month_bonus * bonus_percentage / 100)
    if gross_salary < 12450:
        tax = 0.22
    elif gross_salary < 20000:
        tax = 0.24
    elif gross_salary < 35200:
        tax = 0.30
    elif gross_salary < 60000:
        tax = 0.37
    else:
        tax = 0.45
    net_salary = gross_salary * (1 - tax)

    print(
        f"This month gross salary: {gross_salary:.2f}€. This month net salary: {net_salary:.2f}€. Налог: {tax * 100:.0f}%.")
