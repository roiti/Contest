# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

c = list(raw_input())
n = len(c)
v = 0
for i in xrange(n):
    if c[i] == "o":
        v |= 1 << i

ans = 1000
for pair in xrange(1 << n):
    tmp = 0
    b = 0
    for i in xrange(n):
        if (pair & (1 << i)) > 0:
            tmp += 1
            b |= (v << i) | (v >> (n - i))
    if b & ((1 << n) - 1) == ((1 << n) - 1):
        ans = min(ans, tmp)
print ans
