# coding: utf-8

from collections import Counter

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        lines = [line.rstrip().split('\t')[0] for line in f.readlines()]

    res = '\n'.join(['\t'.join([str(c[1]), c[0]]) for c in Counter(lines).most_common()])

    print(res)
