# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n, m = map(int, raw_input().split())
ans = 0
i = 1
while 1:
    n -= 1
    ans += 1
    if i % m == 0:
        n += 1
    if n == 0: break
    i += 1
print ans
