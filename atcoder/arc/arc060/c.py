# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

N, A = map(int, raw_input().split())
x = map(int, raw_input().split())
dp = [[0]*2505 for i in xrange(55)]
for xi in x:
    for i in xrange(2505 - xi - 1, -1, -1):
        for j in xrange(N, 0, -1):
            dp[j + 1][i + xi] += dp[j][i]
    dp[1][xi] += 1

ans = 0
for j in xrange(1, N + 1):
    ans += dp[j][j*A]
print ans
