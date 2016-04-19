# coding: utf-8

import sys

if __name__ == '__main__':
    n = int(sys.argv[1])

    with open('hightemp.txt', 'r') as f:
        lines = f.readlines()[:n]

    res = '\n'.join([line.rstrip() for line in lines])

    print(res)
