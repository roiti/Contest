# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

ans = [] 
a, b, c = map(int, raw_input().split())
for i in xrange(1, 128):
    if i % 3 == a and i % 5 == b and i % 7 == c:
        ans.append(i)
for i in ans:
    print i
