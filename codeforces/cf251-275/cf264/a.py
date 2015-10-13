# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, s = map(int, raw_input().split())
s *= 100
ans = -1
for i in xrange(n):
    x, y = map(int, raw_input().split())
    if 100 * x + y <= s:
        ans = max(ans, (s - y) % 100)
print ans
