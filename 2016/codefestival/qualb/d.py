# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
A = [int(raw_input()) for i in xrange(N)]
ans = A[0] - 1
d = 2
for i in xrange(1, N):
    ans += (A[i] - 1)/d
    if A[i] == d: d += 1
print ans
