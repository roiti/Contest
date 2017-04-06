# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

def f(b, n):
    if n < b: return n
    return f(b, n/b) + n%b
    
n = int(raw_input())
s = int(raw_input())

for b in xrange(2, 1000000):
    if f(b, n) == s:
        print b
        break
else:
    if n == s:
        print n + 1
    elif n > s:
        print n - s + 1
    else:
        print -1
