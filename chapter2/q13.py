# coding: utf-8

if __name__ == '__main__':
    with open('col1.txt', 'r') as f:
        col1 = [line.rstrip() for line in f.readlines()]

    with open('col2.txt', 'r') as f:
        col2 = [line.rstrip() for line in f.readlines()]

    res = '\n'.join(['\t'.join(c) for c in zip(col1, col2)])

    with open('merged.txt', 'w') as f:
        f.write(res)
