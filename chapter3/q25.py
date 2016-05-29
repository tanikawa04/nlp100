# coding: utf-8

import re

def get_basic_info(text):
    template = re.search(r'(?<=\{\{基礎情報).+?(?=\}\}\n)', text, re.DOTALL).group(0)
    return {k: v for k, v in re.findall(r'\|(.+?) = (.+?)(?<!<br/>)\n', template, re.DOTALL)}

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        text = f.read()

    res = get_basic_info(text)

    print(res)
