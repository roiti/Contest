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

ans = 200 
for i in c:
    if not w: break
    j = bisect.bisect_right(w, i)
    if j >= len(w) - 1: break
    ans = min(ans, w[j + 1] - i + 1)
print ans if ans < 200 else -1
