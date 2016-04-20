# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        lines = [line.rstrip().split('\t') for line in f.readlines()]

    res = '\n'.join(['\t'.join(line) for line in sorted(lines, key=lambda col: float(col[2]), reverse=True)])

    print(res)
