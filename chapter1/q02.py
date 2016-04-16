# coding: utf-8

if __name__ == '__main__':
    text1 = 'パトカー'
    text2 = 'タクシー'

    res = ''.join([a + b for a, b in zip(text1, text2)])

    print(res)
