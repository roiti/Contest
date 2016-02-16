# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, M = map(int, raw_input().split())
S = int(raw_input())
TK = sorted(map(int, raw_input().split()) for i in xrange(N))

t = m = i = ans = 0
while t < S:
    if i < N and TK[i][0] == t:
        m += TK[i][1]
        i += 1
    if m >= M:
        ans += 1
    t += 1
print ans


