# coding: utf-8

import re

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        res = '\n'.join(re.findall(r'(?<=\[\[Category:).*(?=\]\])', f.read()))

    print(res)
