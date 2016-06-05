# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    surfaces = []

    for words in sentences:
        nouns = list(filter(lambda word: word['pos'] == '名詞' and word['pos1'] == 'サ変接続', words))
        surfaces.extend([noun['base'] for noun in nouns])

    res = set(surfaces)

    print(res)
