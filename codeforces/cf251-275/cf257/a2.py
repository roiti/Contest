# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
mx = (max(a) + m - 1) / m
ans = 0
for i in xrange(n):
    if (a[i] + m - 1) / m == mx:
        ans = i
print ans + 1
