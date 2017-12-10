# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

X = raw_input()
S = raw_input()
ans = ""
for si in S:
    if si not in X:
        ans += si
print ans
