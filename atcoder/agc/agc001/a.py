# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
L = map(int, raw_input().split())
L.sort()
ans = 0
for i in xrange(N - 1, -1, -1):
    ans += min(L[2*i], L[2*i + 1])
print ans
