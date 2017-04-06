# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, K = map(int, raw_input().split())
a = map(int, raw_input().split())

ans = 0
for i in xrange(N):
    ans += min(i + 1, N - i, K) * a[i]

print ans
