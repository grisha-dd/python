#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

i = int(input("Введите целое положительное число: "))

max = 0

while i > 1:
    num = i % 10
    if num > max:
        max = num
    i = int (i // 10)
print(max)
