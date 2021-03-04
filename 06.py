#6

from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

my_list = [23, 1, 44, 3, 2, 10, 7]
с = 0
for el in cycle(my_list):
        if с > 3 * len(my_list) - 1:
            break
        print(el)
        с += 1