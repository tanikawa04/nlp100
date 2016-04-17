# coding: utf-8

if __name__ == '__main__':
    with open('hightemp.txt', 'r') as f:
        doc = f.read()

    res = doc.replace('\t', ' ')

    print(res)
