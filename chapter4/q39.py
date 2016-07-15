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
    freqs = [v for k, v in Counter(count.values()).most_common()]

    plt.plot(list(range(len(freqs))), freqs)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
