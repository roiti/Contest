# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
miss = [0]*(N + 1)

ans = -1
for i in xrange(3, N + 2):
    a0, a1 = 1, 1
    if i <= N: miss[i] = 1
    for j in xrange(3, N + 1):
        a0, a1 = a1, a1 + a0 - miss[j]
    if i <= N and a1 < M:
        miss[i] = 0
    elif a1 == M:
        ans = sum(miss[3:])
        break
print ans
