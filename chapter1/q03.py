# coding; utf-8

if __name__ == '__main__':
    text = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    words = text.replace(',', '').replace('.', '').split()
    res = [len(word) for word in words]

    print(res)
