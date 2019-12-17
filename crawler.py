#!/usr/bin/python3
# filename: test.py
# Author: test
# Date: 20191215 18:36:02

import requests
import re
from bs4 import BeautifulSoup

def to_dict(text):
    '''count words in text, return {WROD: COUNT,...}'''
    space = ' '
    s = set(text.split(space))
    o = {i:text.count(i) for i in s if i.isalpha()}
    return o

def to_string(url):
    r = requests.get(url)
    p = re.compile(r'<\?\w[^>]*>')
    o = p.sub('', r.text)
    return o

def count_sum(*d):
    dk = []
    for i in d:
        dk = dk + list(i.keys())

    out = {}
    for word in set(dk):
        count = 0
        for i in d:
            try:
                count = count + i[word]
            except KeyError:
                count = count
        out[word] = count
    return out

def get_links(url):
    r = requests.get(url)
    b = BeautifulSoup(r.text, 'html.parser')
    a = b('a')
    aa = [i.attrs['href'] for i in a ]
    return aa




if __name__ == '__main__':
    url = 'http://' + input('url: ')
    s = to_string(url)
    print(to_dict(s))
