# 1
my_list = [1, 'Abc', False, 4, 10]
print(type(my_list))

# 2
my_list = list(input('Введите элементы списка: '))
l = len(my_list)
i = 0
if l % 2 == 0:
    l = l
else:
    l = l-1

while i <= l - 1:
    a = my_list[i]
    b = my_list[i+1]
    my_list[i] = b
    my_list[i+1] = a
    i=i+2
print(my_list)

# 3
#list - первый способ
my_list = ['winter','spring','summer','autumn']
month_num =int(input('Введите номер месяца: '))
if month_num > 12 or month_num < 1:
    print('Такого месяца нет')
else:

    if month_num in range(3,5):
        i = 1
    elif month_num in range(6,8):
        i = 2
    elif month_num in range(9, 11):
        i = 3
    else:
        i = 0

print(my_list[i])

#dict - второй способ
my_dict = {
12: 'winter',
1: 'winter',
2: 'winter',
3: 'spring',
4: 'spring',
5: 'spring',
6: 'summer',
7: 'summer',
8: 'summer',
9: 'autumn',
10: 'autumn',
11: 'autumn'
}
month = int(input('Введите номер месяца: '))
print(my_dict[month])

#4
my_str = input('Введите слова: ')
w = my_str.split()
for i, w in enumerate(w):
    print(i +1, w[0:10])

#5
my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
l = len(my_list)
i = 0
while i < l:
    if num > my_list[i]:
        my_list.insert(i,num)
        break
    elif i != l - 1:
        i = i + 1
    else:
        my_list.append(num)
        break
print(my_list)

#6

# Программа не рабочая, не получилось в цикле сделать динамическую переменную зависящую от итерации в цикле.
# В цикле for к переменной my_list должен добавляться индекс от 1 до 4 в зависимости от итерации.
# Не знаю как это можно реализовать
my_dict = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
my_list_1 = []
my_list_2 = []
my_list_3 = []
my_list_4 = []
i = 1
q = '0'
while q != 'q':
    for k in my_dict.keys():
        value = input(f'Введите {k}: ')
        ("my_list_" + str(i)).append(value)
        print(my_list_1)
        i = i + 1
    q = input('Для выхода нажмите q: ')
my_dict['название'] = my_list_1
my_dict['цена'] = my_list_2
my_dict['количество'] = my_list_3
my_dict['единица измерения'] = my_list_4
print(my_dict)


