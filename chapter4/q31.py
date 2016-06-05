# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    surfaces = []

    for words in sentences:
        verbs = list(filter(lambda word: word['pos'] == '動詞', words))
        surfaces.extend([verb['surface'] for verb in verbs])

    res = set(surfaces)

    print(res)
