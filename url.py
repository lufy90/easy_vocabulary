#!/bin/usr/python3


import requests
import sys
from bs4 import BeautifulSoup

class Url(str):
    def get_protocol(self):
        return self.split(':')[0]

    def get_hostname(self):
        return self.split('/')[2]

    def get_current(self):
        if self[-1] is '/':
            return self.split('/')[-2]
        else:
            return self.split('/')[-1]

    def get_parent(self):
        if self[-1] is '/':
            return '/'.join(self.split('/')[:-2])
        else:
            return '/'.join(self.split('/')[:-1])
        

class Page():
    def __init__(self,url):
        self.url = Url(url)
        try:
            self.response = requests.get(url)
            self.status = self.response
        except Exception as e:
            print('%s' % e, file=sys.stderr)

    def get_content(self):
        return content

    def get_href(self):
        return href
