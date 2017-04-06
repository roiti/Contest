# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
ans = ""
for si in s:
    if si == "B":
        ans = ans[:-1]
    else:
        ans += si
print ans
