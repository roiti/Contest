# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
ans = 0
for s in S:
    if s.isdigit():
        ans += int(s)
print ans
