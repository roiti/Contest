# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
ab = [map(int, raw_input().split()) for i in xrange(N)]
cd = [map(int, raw_input().split()) for i in xrange(M)]

for i, (a, b) in enumerate(ab):
    mn = 1e10
    p = -1
    for j, (c, d) in enumerate(cd, 1):
        tmp = abs(a - c) + abs(b - d)
        if tmp < mn:
            mn = tmp
            p = j
    print p
