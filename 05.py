#5

from functools import reduce
def my_func(prev_el, el):
    return prev_el * el

my_list = [x for x in range (100,1001) if x % 2 == 0]
print(reduce(my_func, my_list))