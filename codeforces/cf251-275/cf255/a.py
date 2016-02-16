# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())

dp = [[0] * 100001 for i in xrange(2)]

dp[0][0] = dp[1][n - 1] = 1
for i in xrange(n - 1): dp[0][i + 1] = dp[0][i] + 1 if a[i] < a[i + 1] else 1
for i in xrange(n - 2, -1, -1): dp[1][i] = dp[1][i + 1] + 1 if a[i] < a[i + 1] else 1
ans = 1
for i in xrange(n): ans = max(ans, dp[0][i] + 1, dp[1][i] + 1)
for i in xrange(1, n - 1):
    if a[i - 1] + 1 < a[i + 1]:
        ans = max(ans, dp[0][i - 1] + 1 + dp[1][i + 1])

print min(ans, n)
