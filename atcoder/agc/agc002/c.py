# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, L = map(int, raw_input().split())
a = map(int, raw_input().split())
b = [0]*(N - 1)
for i in xrange(N - 1):
    b[i] = a[i] + a[i + 1]

mx, idx = 0, 0
for i, bi in enumerate(b):
    if bi > mx:
        mx = bi
        idx = i

if mx >= L:
    print "Possible"
    for i in xrange(idx):
        print i + 1
    for i in xrange(N - 1, idx, -1):
        print i
else:
    print "Impossible"
