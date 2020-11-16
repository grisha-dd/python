from itertools import count, cycle, islice

my_list = []
print("Итератор а: ")
for el in islice(count(int(input("Enter any number: "))), 5):
    print(el)
    my_list.append(bin(el))

print("Итератор b: ")
for i in islice(cycle(my_list), 7):
    print(i)
