# coding: utf-8

from morph import Morph

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return 'chunk.Chunk({}, {}, {})'.format(self.morphs, self.dst, self.srcs)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def parse_sentence(cabocha_sent):
        chunks = []
        morphs = []
        dependencies = {}

        lines = cabocha_sent.split('\n')

        for line in lines:

            if line.startswith('*'):

                if len(morphs) > 0:
                    chunks.append(Chunk(morphs, dst, [k for k, v in dependencies.items() if v == src]))

                morphs = []

                elems = line.split(' ')
                src, dst = int(elems[1]), int(elems[2][:-1])

                if dst > -1:
                    dependencies[src] = dst

            else:
                morphs.append(Morph.parse(line))

        chunks.append(Chunk(morphs, dst, [k for k, v in dependencies.items() if v == src]))

        return chunks


if __name__ == '__main__':
    cabocha_sent = '''* 0 2D 0/1 -1.911675
名前	名詞,一般,*,*,*,*,名前,ナマエ,ナマエ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
* 1 2D 0/0 -1.911675
まだ	副詞,助詞類接続,*,*,*,*,まだ,マダ,マダ
* 2 -1D 0/0 0.000000
無い	形容詞,自立,*,*,形容詞・アウオ段,基本形,無い,ナイ,ナイ
。	記号,句点,*,*,*,*,。,。,。'''

    print(Chunk.parse_sentence(cabocha_sent))
