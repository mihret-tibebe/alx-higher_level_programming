#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # new_list = None
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
    
my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)
