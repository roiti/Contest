# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

b = raw_input().split()
N = int(raw_input())
a = ["".join(str(b.index(k)) for k in raw_input()) for i in xrange(N)]
a.sort(key = lambda x: int(x))
for ai in a:
    print "".join(b[int(k)] for k in ai)
