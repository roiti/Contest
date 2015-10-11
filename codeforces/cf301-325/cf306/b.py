# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, l, r, x = map(int, raw_input().split())
c = map(int, raw_input().split())

ans = 0 
for m in xrange(1, n + 1):
    for prob in it.combinations(range(n), m):
        s = sum(c[i] for i in prob)
        if l <= s <= r:
            mn = min(c[i] for i in prob)
            mx = max(c[i] for i in prob)
            if mx - mn >= x:
                ans += 1
print ans
