# -*- coding: utf-8 -*-
import sys,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, x = map(int, raw_input().split())
ans = 0
for i in xrange(1, n + 1):
    if x % i == 0 and x / i <= n:
        ans += 1
print ans
