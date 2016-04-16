# coding: utf-8

from q05 import ngram

if __name__ == '__main__':
    text1 = 'paraparaparadise'
    text2 = 'paragraph'

    X = set(ngram(2, text1))
    Y = set(ngram(2, text2))

    union = X.union(Y)
    intersection = X.intersection(Y)
    difference1 = X.difference(Y)
    difference2 = Y.difference(X)

    print('X ∪ Y:', union)
    print('X ∩ Y:', intersection)
    print('X - Y:', difference1)
    print('Y - X:', difference2)

    target = tuple('se')
    
    in_x = target in X
    in_y = target in Y

    print('"se" in X:', in_x)
    print('"se" in Y:', in_y)
