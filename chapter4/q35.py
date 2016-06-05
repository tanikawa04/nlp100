# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko_morphemes.json', 'r') as f:
        sentences = json.loads(f.read())

    phrases = []
    nouns = []

    for words in sentences:
        words.append({'pos': ''})   # 文末にダミー単語を追加

        for word in words:
            if word['pos'] == '名詞':
                nouns.append(word['surface'])
            else:
                if len(nouns) >= 2:
                    phrases.append(''.join(nouns))
                nouns = []

    res = set(phrases)

    print(res)
