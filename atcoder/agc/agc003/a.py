# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

s = raw_input()
N = S = W = E = 0
for si in s:
    if si == "N": N = 1
    if si == "S": S = 1
    if si == "W": W = 1
    if si == "E": E = 1
print "Yes" if N == S and W == E else "No"
