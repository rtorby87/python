#1
from sys import argv

script_name, working_hours, rate, bonus = argv

print("Выработка в часах: ", working_hours)
print("Ставка: ", rate)
print("Премия: ", bonus)

salary = int(working_hours) * float(rate) + float(bonus)
print(salary)