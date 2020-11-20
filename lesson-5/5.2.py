# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open("lesson_5-1_dd.txt", "w+", encoding="utf-8") as task:
    N = input("Введите несколько строк, для окончания введите пустую строку: ")
    while N != "":
        task.write(f"{N}\n")
        N = input()
    print(f"Записать завершена\n")
    task.seek(0)
    q_line = 0
    for line in task:
        q_line += 1
        l_letters = len(line)-1
        print(f"Количество букв в {q_line} строке : {l_letters}")
print(f"Количество строк: {q_line}")
