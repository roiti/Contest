# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

S = raw_input()
T = "CODEFESTIVAL2016"
ans = 0
for s, t in zip(S, T):
    if s != t:
        ans += 1
print ans
