# coding: utf-8

import json
from collections import Counter
import matplotlib.pyplot as plt

def flatten(l):
    flatten_l = []

    for a in l:
        flatten_l += a

    return flatten_l

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    words = [morph['base'] for morph in flatten(sentences)]
    count = Counter(words)

    plt.hist(list(count.values()), bins=100)    # ほとんど何も見えない
    plt.show()
