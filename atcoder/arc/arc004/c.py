# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

X, Y = map(int, raw_input().split("/"))
ans = []
for N in xrange(max(1, 2*X/Y - 5), 2*X/Y + 5):
    A = N*((N + 1)*Y - 2*X)
    B = 2*Y
    if A % B != 0: continue
    M = A / B
    if 1 <= M <= N:
        ans.append((N, M))

if len(ans) == 0:
    print "Impossible"
else:
    for i, j in ans:
        print i, j 

