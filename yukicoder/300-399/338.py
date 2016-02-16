# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B = map(int, raw_input().split())

ans = 1e10
for a in xrange(1000):
    for b in xrange(1, 1000) if a == 0 else xrange(1000):
        if round(100.0*a/(a + b), 0) == A and round(100.0*b/(a + b), 0) == B:
            ans = min(ans, a + b)
print ans
