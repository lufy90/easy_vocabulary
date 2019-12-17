#!/usr/bin/python3
# filename: dict_sum.py
# Author: test
# Date: 20191216 21:50:18

from crawler import count_sum
import unittest

class TestCount(unittest.TestCase):
    def test_anb(self):
        a = {'a':1, 'b':1}
        b = {'a':2, 'c':3}
        c = {'a':3, 'b':1, 'c':3}
        self.assertEqual(count_sum(a,b),c)
    def test_3elements(self):
        a = {'a':1, 'b':2}
        b = {'b':3}
        c = {'c':2}
        d = a
        e = c
        o = count_sum(a,b,c,d,e)
        self.assertEqual(o['a'], 2)
        self.assertEqual(o['b'], 7)
        self.assertEqual(o['c'], 4)


if __name__ == '__main__':
    unittest.main()
