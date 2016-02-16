# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

A, B = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())

dp = [[0] * (A + 5) for i in xrange(B + 5)]
for i in xrange(A):
    for j in xrange(B):
        dp[j][i] = max(dp[j - 2][i] + b[j], dp[j][i - 2] + a[i])

if (A + B) % 2 == 1:
    print dp[B - 1][A - 1]
else:
    print max(dp[B - 2][A - 1], dp[B - 1][A - 2])
