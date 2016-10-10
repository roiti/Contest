# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
mx = 0
t = 0
while N:
    mx = max(mx, t + 2*N)
    t += N
    N /= 2
print mx - t 
