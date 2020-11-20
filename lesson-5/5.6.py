# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого
# предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести словарь на экран. Примеры строк файла: Информатика:   100(л)   50(пр)   20(
# лаб). Физика:   30(л)   —   10(лаб) Физкультура:   —   30(пр)   — Пример словаря: {“Информатика”: 170,
# “Физика”: 40, “Физкультура”: 30}

with open("text_6.txt", "r", encoding="utf-8") as schedule:
    schedule_d = {}
    for line in schedule:
        key, value = line.split(": ")
        value = ("".join([num for num in value if num.isdigit() or num == " "])).split()
        sum_value = 0
        for n in value:
            sum_value += int(n)
        schedule_d[key] = sum_value
    print(schedule_d)