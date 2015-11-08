# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
ans = 0
for h in xrange(n):
    w = map(int, raw_input().split())
    for i in xrange(0, 2*m, 2):
        if sum(w[i:i+2]) > 0:
            ans += 1
print ans
