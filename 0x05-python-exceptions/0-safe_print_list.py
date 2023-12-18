#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    new_list = []
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            new_list.append(my_list[i])
            count = count + 1
        print()
    except IndexError:
        print("Out of index")

    return count
