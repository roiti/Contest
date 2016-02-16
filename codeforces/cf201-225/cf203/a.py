# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
a = sorted(map(int, raw_input().split()))
b = sorted(map(int, raw_input().split()))

for v in xrange(max(a), min(b)):
    if v/2 >= a[0]:
        print v
        break
else:
    print -1
