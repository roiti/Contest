# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
a, b = [], []
for i in xrange(M):
    ai, bi = map(int, raw_input().split())
    a.append(ai)
    b.append(bi)

l = mxr = 0
ans = 0
while l < N:
    for i in xrange(M):
       if a[i] <= l + 1:
           mxr = max(mxr, b[i])
    if l == mxr:
        break
    l = mxr
    ans += 1

print ans if l == N else "Impossible"
    
