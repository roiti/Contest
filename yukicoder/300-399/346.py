# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()

c = []
w = []
for i, si in enumerate(s):
    if si == "c":
        c.append(i)
    if si == "w":
        w.append(i)

ans = 0 
for i in c:
    j = bisect.bisect_right(w, i)
    if j >= len(w) - 1: break
    ans += (len(w) - j - 1)*(len(w) - j)/2
print ans
