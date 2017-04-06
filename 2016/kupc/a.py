# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, A, B = map(int, raw_input().split())
t = [int(raw_input()) for i in xrange(N)]

ans = N
for ti in t:
    if A <= ti < B: ans -= 1
print ans
