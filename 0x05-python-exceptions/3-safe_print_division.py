#!/usr/bin/python3

def safe_print_division(a, b):
    result = 0
    flag = False
    try:
        result = a / b
    except ZeroDivisionError:
        flag = True
    finally:
        if flag is True:
            print("Inside result: {}".format(None))
            return None
        print("Inside result: {}".format(result))
        return result
