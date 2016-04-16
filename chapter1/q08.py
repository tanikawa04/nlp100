# coding: utf-8

def cipher(text):
    return ''.join([chr(219 - ord(c)) if c.islower() else c for c in text])

if __name__ == '__main__':
    text = 'Hope for the best, but prepare for the worst.'

    e = cipher(text)
    d = cipher(e)

    print('original:', text)
    print(' encrypt:', e)
    print(' decrypt:', d)
