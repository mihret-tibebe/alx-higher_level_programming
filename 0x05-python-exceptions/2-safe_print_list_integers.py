#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end='')
                count = count + 1
            continue
        print()

    except TypeError:
        print('')
    except ValueError:
        print('')
    except IndexError as err:
        raise IndexError('list index out of range')

    return count
