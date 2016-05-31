# coding: utf-8

import json

if __name__ == '__main__':
    with open('neko.txt.mecab', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    sentences = []
    morphemes = []
    for line in lines:
        if line in 'EOS':
            if len(morphemes) > 0:
                sentences.append(morphemes)
                morphemes = []
        else:
            surface, feature = line.split('\t')
            elems = feature.split(',')
            morphemes.append({'surface': surface, 'base': elems[6], 'pos': elems[0], 'pos1': elems[1]})

    print(sentences)
    
    with open('neko_morphemes.json', 'w') as f:
        f.write(json.dumps(sentences))
