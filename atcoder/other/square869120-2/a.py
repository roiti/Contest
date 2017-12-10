# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
ans = 0
i = o = False
for c in S:
    if c == "I":
        if not i:
            i = True
        elif o:
            ans += 2
            o = False
    else:
        o = True
print ans
