# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A = list(raw_input())
B = list(raw_input())

n = len(A)
m = len(B)

ans = 0
for i in xrange(n - m + 1):
    if A[i:i + m] == B:
        A[i + m - 1] = "#"
        ans += 1
print ans
