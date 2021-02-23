# # 1
# def my_func(number_1, number_2):
#     try:
#         answer = float(number_1) / float(number_2)
#     except ZeroDivisionError:
#         return 'Деление на ноль!'
#     return answer
#
# a = my_func(input('Введите первое число: '), input('Введите второе число: '))
# print (a)

# #2
#
# def my_func(**kwargs):
#     return kwargs
#
# a = my_func(name = input('Введите имя: '), surname = input('Введите фамилию: '), dob =input('Введите дату рождения: '),
# email = input('Введите email: '), num = input('Введите телефон: '))
#
# print(a)

# #3
#
# def my_func(number_1, number_2, number_3):
#     old_list = [number_1, number_2, number_3]
#     new_list = []
#     f_min = min(number_1, number_2, number_3)
#     i = 0
#     while i < len(old_list):
#      if old_list[i] != f_min:
#          new_list.append(old_list[i])
#      i = i + 1
#     a = sum(new_list)
#     return a
#
# print(my_func(int(input()), int(input()), int(input())))

# # 4
# def my_func(x, y):
#     m = x ** y
#     return m
#
# print (my_func(int(input()), int(input())))

# 5

# def my_func():
#     full_sum = 0
#     q = '0'
#     while q != 'q':
#         my_sum = 0
#         numbers = input('Введите числа ').split()
#         for number in numbers:
#             my_sum = my_sum + int(number)
#         full_sum = full_sum + my_sum
#         q = input('Для выхода нажмите q ')
#     return full_sum
#
# print (my_func())

# 6

def my_func(text):
    return text.title()

print(my_func(input()))
