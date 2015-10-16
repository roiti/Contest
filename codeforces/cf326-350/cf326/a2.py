# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
ap = [map(int, raw_input().split()) for i in xrange(n)]

ans = 0
mn = 10000
for i in xrange(n):
    a, p = ap[i]
    if p < mn:
        mn = p
    ans += a * mn
print ans

