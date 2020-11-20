# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open("lesson_5_5_dd.txt", "w+", encoding="utf-8") as gen_num:
    gen_num.write(" ".join([f"{randint(0, 1000)}" for _ in range(20)]))
    gen_num.seek(0)
    sum_num = 0
    for i in gen_num.read().split():
        sum_num += int(i)
    print(sum_num)
