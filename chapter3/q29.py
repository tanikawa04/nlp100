# coding: utf-8

import urllib.parse
import urllib.request
import json
from q25 import get_basic_info

if __name__ == '__main__':
    with open('britain.txt', 'r') as f:
        text = f.read()

    d = get_basic_info(text)

    params_str = urllib.parse.urlencode({
        'action': 'query',
        'prop': 'imageinfo',
        'titles': 'File:{0}'.format(d['国旗画像']),
        'iiprop': 'url',
        'format': 'json'
    })

    with urllib.request.urlopen('https://www.mediawiki.org/w/api.php?{0}'.format(params_str)) as response:
        res = json.loads(response.read().decode('utf-8'))['query']['pages']['-1']['imageinfo'][0]['url']

    print(res)
