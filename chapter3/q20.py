# coding: utf-8

import gzip
import json

if __name__ == '__main__':
    docs = {}
    with gzip.open('jawiki-country.json.gz', 'r') as f:
        for line in f.readlines():
            doc = json.loads(line.decode('utf-8'))
            docs[doc['title']] = doc['text']

    britain = docs['イギリス']
    print(britain)

    with open('britain.txt', 'w') as f:
        f.write(britain)
