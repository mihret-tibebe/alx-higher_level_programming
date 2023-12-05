#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None

    for i in reversed(range(len(my_list))):
        print("{:d}".format(my_list[i]))


# print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = None
print_reversed_list_integer(my_list)