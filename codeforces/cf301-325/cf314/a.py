# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
x = [-1e18] + map(int, raw_input().split()) + [1e18]

for i in xrange(1, n + 1):
    mn = min(x[i] - x[i - 1], x[i + 1] - x[i])
    mx = max(x[i] - x[1], x[n] - x[i])
    print mn, mx
