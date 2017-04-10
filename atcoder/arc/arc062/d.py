# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
N = len(s)
g, p = 0, 0
ans = 0
for si in s:
    if si == "g":
        if g > p:
            ans += 1
            p += 1
        else:
            g += 1
    else:
        if g > p:
            p += 1
        else:
            ans -= 1
            g += 1
print ans
