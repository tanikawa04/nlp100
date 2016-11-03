# coding: utf-8

from chunk import Chunk

if __name__ == '__main__':
    with open('neko.txt.cabocha', 'r') as f:
        cabocha_sents = [cabocha_sent.strip() for cabocha_sent in f.read().split('EOS') if cabocha_sent != '\n']

    chunks = Chunk.parse_sentence(cabocha_sents[7])

    print(chunks)
