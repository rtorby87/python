#2

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in enumerate(old_list) if el > old_list[i - 1] and el != old_list[0]]
print (new_list)
