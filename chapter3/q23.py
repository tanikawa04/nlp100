# coding: utf-8

import re

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        section_lines = [(match[1], len(match[0]) - 1) for match in re.findall(r'^(={2,})(.+)\1$', f.read(), re.MULTILINE)]

    res = '\n'.join(['\t'.join([cols[0], str(cols[1])]) for cols in section_lines])

    print(res)
