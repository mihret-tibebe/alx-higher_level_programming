#!/usr/bin/python3
import sys
if __name__ == '__main__':
    len = len(sys.argv)
    result = 0
    for index in range(len):
        if index == 0:
            continue
        result += int(sys.argv[index])
    print(result)
