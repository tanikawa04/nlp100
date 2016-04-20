# coding: utf-8

# 注意: ファイルを N 行のごとに分割しています（問題の仕様と違う？）

import sys

if __name__ == '__main__':
    n = int(sys.argv[1])

    with open('hightemp.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    docs = [lines[i:i+n] for i in range(0, len(lines), n)]

    for i, doc in enumerate(docs):
        with open('out-{0}.txt'.format(i), 'w') as f:
            f.write('\n'.join(doc))
            # f.write('\n')
