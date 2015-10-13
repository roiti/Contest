# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

btn = ["A", "B", "X", "Y"]
seq = []
for i in xrange(4):
    for j in xrange(4):
        seq.append(btn[i] + btn[j])

N = int(raw_input())
c = raw_input()
ans = len(c)
for L in seq:
    d = c.replace("".join(L), "L")
    for R in seq:
        e = d.replace(R, "R")
        ans = min(ans, len(e))
print ans
