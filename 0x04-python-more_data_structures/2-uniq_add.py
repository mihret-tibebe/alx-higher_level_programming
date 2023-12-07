#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    sum = 0
    for i in uniq_list:
        sum += i
    return sum

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
