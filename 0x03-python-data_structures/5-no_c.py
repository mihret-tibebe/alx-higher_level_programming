#!/usr/bin/python3

def no_c(my_string):
    result = ''
    for c in my_string:
        if c == 'c' or c == 'C':
            c = ''
        result += c

    return result

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))