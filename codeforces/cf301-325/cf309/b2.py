# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = [map(int, list(raw_input())) for i in xrange(n)]

ans = 0
for i in xrange(n):
    clean = 0
    sweap = set([j for j in xrange(n) if a[i][j] == 0])
    for j in xrange(n):
        duty = set([k for k in xrange(n) if a[j][k] == 0])
        if duty == sweap:
            clean += 1
    ans = max(ans, clean)
print ans

