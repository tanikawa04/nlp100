# coding: utf-8

from morph import Morph

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        cabocha_sents = [cabocha_sent.strip() for cabocha_sent in f.read().split('EOS') if cabocha_sent != '\n']

    sentences = [Morph.parse(cabocha_sent) for cabocha_sent in cabocha_sents]

    print(sentences[2])
