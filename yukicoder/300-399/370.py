# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
D = [int(raw_input()) for i in xrange(M)]
D.sort()

ans = 1e10 
for i in xrange(M - N + 1):
    if D[i] < 0 and D[i + N - 1] > 0:
        ans = min(ans, 2*min(abs(D[i]), abs(D[i + N - 1])) + max(abs(D[i]), abs(D[i + N - 1])))
    else:
        ans = min(ans, max(abs(D[i]), abs(D[i + N - 1])))
print ans
