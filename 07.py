#7

from math import factorial
from itertools import count


def fact():
    for el in count(1):
        yield factorial(el)

f = int(input("Введите конечное кол-во элементов факториала: "))

for i, factor in enumerate(fact(),1):
    if i > f:
        break
    print(i, factor)