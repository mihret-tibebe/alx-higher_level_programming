#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, value in a_dictionary:
        new_dict[key] = list(map(lambda x: x * 2, value))

    return new_dict
