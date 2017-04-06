# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
A = map(int, raw_input().split())
A.sort()

ans = 0
for i in xrange(K):
    ans += A[i] + i
print ans
