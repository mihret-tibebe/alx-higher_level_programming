#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    if len == 1:
        print('0 arguments.')
    elif len == 2:
        print('1 argument:')
        print("1:", format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(len - 1))
        for index in range(len):
            if index == 0:
                continue
            print("{:d}: {}".format(index, sys.argv[index]))
