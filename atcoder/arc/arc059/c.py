# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
a = map(int, raw_input().split())
ans = 1e10
for b in xrange(-100, 101):
    tmp = 0
    for ai in a:
        tmp += (ai - b)**2
    ans = min(ans, tmp)
print ans

