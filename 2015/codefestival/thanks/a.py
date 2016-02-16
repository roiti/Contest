# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A = int(raw_input())
B = int(raw_input())

ans = abs(A)
if 0 < B < A or A < B < 0:
    ans += abs(A)
elif 0 < A < B or B < A < 0:
    ans += abs(A - B) + abs(B)
else:
    ans += abs(A) + 2*abs(B)
print ans
