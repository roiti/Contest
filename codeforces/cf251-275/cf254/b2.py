# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

fa = [0] * 101
def gf(x):
    if fa[x] != x: fa[x] = gf(fa[x])
    return fa[x]

n, m = map(int, raw_input().split())
for i in xrange(n): fa[i] = i
for loop in xrange(m):
    x, y = map(int, raw_input().split()) 
    x -= 1; y -= 1
    fa[gf(x)] = gf(y)

ans = 2 ** n
for i in xrange(n):
    if gf(i) == i:
        ans /= 2
print ans
