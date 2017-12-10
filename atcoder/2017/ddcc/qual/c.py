# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, C = map(int, raw_input().split())
L = sorted([int(raw_input()) for i in xrange(N)])
ans = N
i, j = 0, N - 1
while i < j:
    while i < j and L[i] + L[j] + 1 > C:
        j -= 1
    if L[i] + L[j] + 1 <= C:
        ans -= 1
        j -= 1
    i += 1

print ans
