# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить
# подсчет средней величины дохода сотрудников. Пример файла: Иванов 23543.12 Петров 13749.32

print("Сотрудники с окладом не менее 20 тысяч:")
with open("text_3.txt", "r", encoding="utf-8") as info:
    d_info = {}
    # d_info = {line.split()[0]: float(line.split()[1]) for line in f}
    for line in info:
        key, value = line.split()
        d_info[key] = float(value)
        if d_info[key] > 20000:
            print(key)
print(f"\nСредний оклад:")
print(sum(d_info.values()) / len(d_info))