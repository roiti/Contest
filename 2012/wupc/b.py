# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
S = [raw_input() for i in xrange(N)]
ans = "z"*100
for i in xrange(N):
    for j in xrange(N):
        if i == j: continue
        ans = min(ans, S[i] + S[j])
print ans
