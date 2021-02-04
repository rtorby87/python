#1
n = 5
print (n)

#2

sec = input("Введите секунды: ")
h = int(sec)// 3600
m = int(sec)//60
print (f' HH: {h},MI: { m - 60*h}, SS: {int(sec) -60*(m - h*60 ) - 3600*h}')

#3

n = input("Введите число: ")
print (int(n) + int(n+ n) + int(n+ n+ n))

#4

n = int (input("Введите число: "))
m = n % 10
d = n // 10
while d > 0:
    if d % 10 > m:
        m = d % 10
    d = d // 10
print (m)

#5

income = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
rent = (income - costs)/ income
if income > costs:
    print("Фирма показывает прибыль")
    print ("Рентабельность: ", rent )
    emp = int(input("Введите количество сотрудников: "))
    e = (income - costs) / emp
    print( "Прибыль на одного сотрудника: ", e)
elif income < costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает в 0")

# 6

a = int(input("Введите результат первого дня: "))
b = int(input("Введите требуемый результат: "))
i = 1
while a <= b:
    i += 1
    a = a * 1.1
    print (i, a)
print ("Номер дня: ", i)



