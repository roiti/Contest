# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
T, A = 1, 1 
for loop in xrange(N):
    t, a = map(int, raw_input().split())
    n = max((T + t - 1)/t, (A + a - 1)/a)
    T, A = n*t, n*a
print T + A

