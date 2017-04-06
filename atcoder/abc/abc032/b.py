# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
k = int(raw_input())
n = len(s)
c = set()
for i in xrange(n):
    if i + k > n: break
    c.add(s[i:i + k])

print len(c)
