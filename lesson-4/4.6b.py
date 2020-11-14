from itertools import cycle

i = 0
for el in cycle("This is my list".split()):
    if i > 7:
        break
    i += 1
    print(el)
