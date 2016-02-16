# -*- coding: utf-8 -*-
import sys,copy,math,heapq,itertools as it,fractions,re,bisect,collections as coll

n = int(raw_input())
a = map(int, raw_input().split())
cnt = [0] * (10 ** 5 + 10)
for ai in a:
    cnt[ai] += 1

dp = [[0, 0] for i in xrange(10 ** 5 + 10)]
for i in xrange(1, 10 ** 5 + 1):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    dp[i][1] = dp[i - 1][0] + cnt[i] * i
print max(dp[10 ** 5])
