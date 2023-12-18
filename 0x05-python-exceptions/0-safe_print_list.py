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


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
