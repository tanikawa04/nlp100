# coding: utf-8

def ngram(n, seq):
    res = []
    for i in range(len(seq) - n + 1):
        res.append(tuple(seq[i:i+n]))
    return res

if __name__ == '__main__':
    text = 'I am an NLPer'

    res1 = ngram(2, text.split())
    res2 = ngram(2, text)

    print(res1)
    print(res2)
