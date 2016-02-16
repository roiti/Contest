# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N = int(raw_input())
dp = [0] * 1601 
for i in xrange(1, 7):
    dp[i] = 1
for i in xrange(N - 1):
    ndp = [0] * 1601
    for j in xrange(1600, 0, -1):
        for k in xrange(max(j - 6, 0), j):
            ndp[j] += dp[k]
    dp = ndp[:]

ans = 0
mx = 0
for i in xrange(1600):
    if dp[i] > mx:
        mx = dp[i]
        ans = i
print ans
