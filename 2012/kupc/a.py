# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, T, E = map(int, raw_input().split())
x = map(int, raw_input().split())
ans = -1
for i in xrange(N):
    if min(T%x[i], x[i] - T%x[i]) <= E:
        ans = i + 1
print ans
