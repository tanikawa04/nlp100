# coding: utf-8

def template(x, y, z):
    return '{0}時の{1}は{2}'.format(x, y, z)

if __name__ == '__main__':
    x = 12
    y = '気温'
    z = 22.4

    res = template(x, y, z)

    print(res)
