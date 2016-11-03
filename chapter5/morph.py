# coding: utf-8

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return '''morph.Morph('{}', '{}', '{}', '{}')'''.format(self.surface, self.base, self.pos, self.pos1)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def parse(cabocha_morph):
        surface, feature = cabocha_morph.split('\t')
        elems = feature.split(',')
        return Morph(surface, elems[6], elems[0], elems[1])


if __name__ == '__main__':
    cabocha_txt = '名前\t名詞,一般,*,*,*,*,名前,ナマエ,ナマエ'

    print(Morph.parse(cabocha_txt))
