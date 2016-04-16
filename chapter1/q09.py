# coding: utf-8

from random import shuffle

def typoglycemia(text):
    words = text.split()
    new_words = []

    for word in words:
        if len(word) > 5:
            head = word[0]
            tail = word[-1]
            body_chars = list(word[1:-1])
            shuffle(body_chars)
            new_words.append(''.join([head, ''.join(body_chars), tail]))
        else:
            new_words.append(word)

    return ' '.join(new_words)

if __name__ == '__main__':
    text = 'I couldn\'t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

    res = typoglycemia(text)

    print(res)
