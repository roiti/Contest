# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
A = map(int, raw_input().split())
B = map(int, raw_input().split())
A.sort()
B.sort()
i = j = 0
while i < N and j < M:
    if A[i] >= B[j]:
        j += 1
    i += 1
print "YES" if j == M else "NO"
