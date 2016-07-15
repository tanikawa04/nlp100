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
    n = 10

    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    words = [morph['base'] for morph in flatten(sentences)]
    count = Counter(words)
    labels, ys = zip(*[c for c in count.most_common(n)])
    xs = list(range(n))

    plt.bar(xs, ys, align='center')
    plt.xticks(xs, labels)
    plt.xlim(-1)    # デザイン調整
    plt.show()
