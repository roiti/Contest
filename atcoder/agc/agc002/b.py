# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
a = [-1]*N
a[0] = 1 
for i in xrange(M):
    x, y = map(int, raw_input().split())
    x, y = x - 1, y - 1
    if a[x] >= 1:
        a[y] = abs(a[y]) + 1
        a[x] -= 1
    elif a[x] <= -1:
        if a[y] <= 0:
            a[y] = a[y] - 1
        elif a[y] > 0:
            a[y] += 1
        a[x] += 1
ans = 0
for ai in a:
    if ai > 0:
        ans += 1
print ans
