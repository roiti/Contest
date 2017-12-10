# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, P = map(int, raw_input().split()) 
A = map(int, raw_input().split()) 

ans = 0
zero = 1
one = 0
for i in xrange(N):
    if A[i] % 2 == 0:
        zero *= 2
        one *= 2
    else:
        zero, one = zero + one, zero + one

print zero if P == 0 else one

