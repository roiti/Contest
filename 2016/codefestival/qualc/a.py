# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
c, f = 1e10, -1
for i, si in enumerate(s):
    if si == "C":
        c = min(c, i)
    if si == "F":
        f = max(f, i)
print "Yes" if c < f else "No"
