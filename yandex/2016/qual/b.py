# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

D, T = map(float, raw_input().split())
N = int(raw_input())
ans, idx = 1e10, 0
for i in xrange(N):
    X, t = map(float, raw_input().split())
    cur = D*(T + t) + X
    if cur < ans:
        ans = cur
        idx = i + 1
print ans, idx
