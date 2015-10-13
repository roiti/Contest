# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
s = raw_input()
t = ""
ans = 0
for si in s:
    t += si
    ans += 1
    while ans > 1 and t[-2:] in ["10", "01"]:
        t = t[:-2]
        ans -= 2
print ans
