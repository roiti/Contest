# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
ans = 0
l = 1
while 10 ** l <= n:
    ans += l * (10 ** l - 10 ** (l - 1))
    l += 1
ans += (n - 10 ** (l - 1)  + 1) * l
print ans
