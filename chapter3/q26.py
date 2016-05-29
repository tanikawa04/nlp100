# coding: utf-8

import re
from q25 import get_basic_info

def remove_emphasis_expression(text):
    return re.sub(r'(\'{2,3}|\'{5})(.+?)\1', r'\2', text)

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        text = f.read()

    d = get_basic_info(text)
    res = {k: remove_emphasis_expression(v) for k, v in d.items()}

    print(res)
