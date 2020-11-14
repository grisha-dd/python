from itertools import count

start_number = int(input("Enter any number: "))
for el in count(start_number):
    if el > start_number + 10:
        break
    print(el)
