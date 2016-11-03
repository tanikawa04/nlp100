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
    def parse(cabocha_sent):
        lines = cabocha_sent.split('\n')
        morphs = []

        for line in lines:
            if not line.startswith('*'):
                surface, feature = line.split('\t')
                elems = feature.split(',')
                morphs.append(Morph(surface, elems[6], elems[0], elems[1]))

        return morphs
