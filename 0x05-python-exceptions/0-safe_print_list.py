#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []
    try:
        for i in range(x):
            print(1, end= '')
            new_list.append(i)
    except IndexError:
        print("Out of index")

    return new_list
