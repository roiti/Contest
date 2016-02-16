# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
k = 0
a = []
for i in xrange(n):
    a.append(1)
    k += 1
    while k >= 2 and a[-1] == a[-2]:
        a.pop()
        a[-1] += 1
        k -= 1

print " ".join(map(str, a))
