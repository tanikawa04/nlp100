# coding: utf-8

from morph import Morph

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        cabocha_sents = [cabocha_sent.strip() for cabocha_sent in f.read().split('EOS') if cabocha_sent != '\n']

    morphs = []
    cabocha_lines = cabocha_sents[2].split('\n')

    for line in cabocha_lines:
        if not line.startswith('*'):
            morphs.append(Morph.parse(line))

    print(morphs)
