# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, Q = map(int, raw_input().split())
a = [0]*N
for loop in xrange(Q):
    L, R, T = map(int, raw_input().split())
    L -= 1
    R -= 1
    for i in xrange(L, R + 1):
        a[i] = T

for ai in a:
    print ai
