# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
ans = 0
for i in xrange(2, n):
    j = 2
    while j * j <= i:
        if i % j == 0:
            break
        j += 1
    else:
        ans += 1
print ans
