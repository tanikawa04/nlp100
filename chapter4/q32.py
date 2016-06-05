# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    bases = []

    for words in sentences:
        verbs = list(filter(lambda word: word['pos'] == '動詞', words))
        bases.extend([verb['base'] for verb in verbs])

    res = set(bases)

    print(res)
