# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    phrases = []

    for words in sentences:
        for i in range(1, len(words) - 1):
            if words[i]['surface'] == 'の' and words[i-1]['pos'] == '名詞' and words[i+1]['pos'] == '名詞':
                phrases.append('{0}の{1}'.format(words[i-1]['surface'], words[i+1]['surface']))

    res = set(phrases)

    print(res)
